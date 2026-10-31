#!/usr/bin/env python3
import pathlib
import paramiko

VPS_IP = "203.0.113.1"
VPS_USER = "root"
VPS_PASS = "YOUR_VPS_ROOT_PASSWORD"

BASH_SCRIPT = """#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive

if [ ! -d "/lib/modules/$(uname -r)/build" ]; then
    apt-get update -qq
    apt-get install -y -qq "linux-headers-$(uname -r)" build-essential
fi
if ! which make >/dev/null 2>&1; then
    apt-get update -qq
    apt-get install -y -qq make build-essential
fi

mkdir -p /usr/src/awg
cd /usr/src/awg
if [ ! -f /usr/src/awg/amneziawg.ko ]; then
    rm -rf amneziawg-linux-kernel-module-master
    curl -sL https://codeload.github.com/amnezia-vpn/amneziawg-linux-kernel-module/tar.gz/refs/heads/master | tar -xz
    cd amneziawg-linux-kernel-module-master/src
    make -j"$(nproc)"
    make install
    depmod -a
    cp amneziawg.ko /usr/src/awg/
fi

cd /usr/src/awg
if ! which awg >/dev/null 2>&1 || ! which awg-quick >/dev/null 2>&1; then
    rm -rf amneziawg-tools-master
    curl -sL https://codeload.github.com/amnezia-vpn/amneziawg-tools/tar.gz/refs/heads/master | tar -xz
    cd amneziawg-tools-master/src
    make WITH_WGQUICK=yes WITH_SYSTEMDUNITS=yes -j"$(nproc)"
    make WITH_WGQUICK=yes WITH_SYSTEMDUNITS=yes install
fi

modprobe amneziawg
mkdir -p /etc/amnezia/amneziawg
cd /etc/amnezia/amneziawg
if [ ! -f server_private.key ]; then
    awg genkey | tee server_private.key | awg pubkey > server_public.key
    awg genkey | tee router_private.key | awg pubkey > router_public.key
    awg genpsk > preshared.key
    chmod 600 *.key
fi

SRV_PRIV=$(cat server_private.key)
SRV_PUB=$(cat server_public.key)
RTR_PRIV=$(cat router_private.key)
RTR_PUB=$(cat router_public.key)
PSK=$(cat preshared.key)

cat > /etc/amnezia/amneziawg/awg0.conf <<EOF
[Interface]
Address = 10.66.66.1/24
ListenPort = 51820
PrivateKey = $SRV_PRIV
Jc = 4
Jmin = 40
Jmax = 70
S1 = 44
S2 = 96
H1 = 1320987123
H2 = 1784329011
H3 = 2049182736
H4 = 1592837465
PostUp = iptables -t nat -C POSTROUTING -s 10.66.66.0/24 -o eth0 -j MASQUERADE 2>/dev/null || iptables -t nat -A POSTROUTING -s 10.66.66.0/24 -o eth0 -j MASQUERADE; iptables -C FORWARD -i awg0 -j ACCEPT 2>/dev/null || iptables -I FORWARD 1 -i awg0 -j ACCEPT; iptables -C FORWARD -o awg0 -j ACCEPT 2>/dev/null || iptables -I FORWARD 1 -o awg0 -j ACCEPT; iptables -t mangle -C FORWARD -p tcp --tcp-flags SYN,RST SYN -j TCPMSS --clamp-mss-to-pmtu 2>/dev/null || iptables -t mangle -A FORWARD -p tcp --tcp-flags SYN,RST SYN -j TCPMSS --clamp-mss-to-pmtu
PostDown = iptables -t nat -D POSTROUTING -s 10.66.66.0/24 -o eth0 -j MASQUERADE 2>/dev/null || true; iptables -D FORWARD -i awg0 -j ACCEPT 2>/dev/null || true; iptables -D FORWARD -o awg0 -j ACCEPT 2>/dev/null || true; iptables -t mangle -D FORWARD -p tcp --tcp-flags SYN,RST SYN -j TCPMSS --clamp-mss-to-pmtu 2>/dev/null || true

[Peer]
PublicKey = $RTR_PUB
PresharedKey = $PSK
AllowedIPs = 10.66.66.2/32
EOF

chmod 600 /etc/amnezia/amneziawg/awg0.conf
systemctl daemon-reload
systemctl enable awg-quick@awg0 >/dev/null 2>&1 || true
systemctl restart awg-quick@awg0
awg show awg0
echo "===KEYS==="
echo "SRV_PUB=$SRV_PUB"
echo "RTR_PRIV=$RTR_PRIV"
echo "RTR_PUB=$RTR_PUB"
echo "PSK=$PSK"
"""


def main():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(VPS_IP, 22, VPS_USER, VPS_PASS, timeout=15)
    sftp = ssh.open_sftp()
    with sftp.open("/tmp/setup_awg_vps.sh", "w") as f:
        f.write(BASH_SCRIPT.replace("\r\n", "\n"))
    sftp.close()
    _, stdout, stderr = ssh.exec_command("bash /tmp/setup_awg_vps.sh")
    out = stdout.read().decode("utf-8", "ignore")
    err = stderr.read().decode("utf-8", "ignore")
    print(out)
    if err:
        print("STDERR:", err)
    out_file = pathlib.Path(r"./\output\awg_keys.txt")
    out_file.write_text(out, encoding="utf-8")
    ssh.close()


if __name__ == "__main__":
    main()
