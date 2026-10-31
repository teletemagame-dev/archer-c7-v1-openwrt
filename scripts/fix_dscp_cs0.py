import paramiko
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5.0)
sock.bind(('192.168.1.110', 0))
sock.connect(('192.168.1.1', 22))
t = paramiko.Transport(sock)
t.connect()
t.auth_none('root')
ssh = paramiko.SSHClient()
ssh._transport = t

cmd = """
# 1. Add DSCP CS0 normalization for 203.0.113.1 in mangle_postrouting (and persist in start_vpn.sh)
nft flush chain inet fw4 mangle_postrouting
nft add rule inet fw4 mangle_postrouting ip daddr 203.0.113.1 ip dscp set cs0

if ! grep -q "ip dscp set cs0" /etc/amnezia/start_vpn.sh; then
    sed -i '/nft flush chain inet fw4 mangle_prerouting/i nft flush chain inet fw4 mangle_postrouting 2>/dev/null || true\\nnft add rule inet fw4 mangle_postrouting ip daddr 203.0.113.1 ip dscp set cs0' /etc/amnezia/start_vpn.sh
fi

# 2. Reload fresh amneziawg.ko.gz just in case and test handshake
ip link del awg0 2>/dev/null || true
rmmod amneziawg 2>/dev/null || true
zcat /etc/amnezia/amneziawg.ko.gz > /tmp/amneziawg.ko && insmod /tmp/amneziawg.ko && rm -f /tmp/amneziawg.ko
ip link add dev awg0 type amneziawg
awg setconf awg0 /etc/amnezia/awg0.conf
ip addr replace 10.66.66.2/24 dev awg0
ip link set mtu 1412 qlen 2000 up dev awg0
ip route replace 192.168.1.0/24 dev br-lan table 66
ip route replace default dev awg0 table 66

ping -c 3 -W 2 -I awg0 10.66.66.1
ip route replace 1.0.0.1/32 dev awg0
while ip rule del fwmark 0x66 lookup 66 2>/dev/null; do :; done
ip rule add fwmark 0x66 lookup 66 priority 100
awg show
ip rule show
"""
stdin, stdout, stderr = ssh.exec_command(cmd)
print(stdout.read().decode('utf-8', errors='replace') + stderr.read().decode('utf-8', errors='replace'))
ssh.close()
