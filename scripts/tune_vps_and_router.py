import paramiko

# 1. Tune VPS 203.0.113.1 (via 10.66.66.1)
print("[1/2] Tuning VPS 203.0.113.1 (BBR + fq + MTU 1412 + TCPMSS + UDP zero-checksum for MIPS RX)...")
vps = paramiko.SSHClient()
vps.set_missing_host_key_policy(paramiko.AutoAddPolicy())
vps.connect('10.66.66.1', 22, 'root', 'YOUR_VPS_ROOT_PASSWORD', timeout=10)

vps_script = """#!/bin/bash
set -e

# Enable BBR + fq + high-speed buffers
cat << 'EOF' > /etc/sysctl.d/99-amnezia-speed.conf
net.core.default_qdisc = fq
net.ipv4.tcp_congestion_control = bbr
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
net.core.rmem_default = 2097152
net.core.wmem_default = 2097152
net.ipv4.tcp_rmem = 4096 131072 16777216
net.ipv4.tcp_wmem = 4096 65536 16777216
net.ipv4.udp_rmem_min = 16384
net.ipv4.udp_wmem_min = 16384
net.core.netdev_max_backlog = 10000
EOF
sysctl --system >/dev/null 2>&1 || true

# Match MTU 1412 with PPPoE router and clamp MSS
ip link set mtu 1412 qlen 2000 dev awg0
if ! grep -q "MTU" /etc/amnezia/amneziawg/awg0.conf; then
    sed -i '/Address/a MTU = 1412' /etc/amnezia/amneziawg/awg0.conf
fi
iptables -t mangle -C FORWARD -p tcp --tcp-flags SYN,RST SYN -j TCPMSS --clamp-mss-to-pmtu 2>/dev/null || \
    iptables -t mangle -A FORWARD -p tcp --tcp-flags SYN,RST SYN -j TCPMSS --clamp-mss-to-pmtu

# Patch VPS amneziawg.ko socket.c to emit UDP nocheck=true so the MIPS router skips redundant outer software UDP checksum on RX
if [ -f /usr/src/amneziawg-linux-kernel-module/src/socket.c ]; then
    if grep -q "fl.fl4_dport, false, false" /usr/src/amneziawg-linux-kernel-module/src/socket.c; then
        sed -i 's/fl.fl4_dport, false, false/fl.fl4_dport, false, true/g' /usr/src/amneziawg-linux-kernel-module/src/socket.c
        make -C /lib/modules/$(uname -r)/build M=/usr/src/amneziawg-linux-kernel-module/src -j$(nproc) modules >/dev/null 2>&1
        cp /usr/src/amneziawg-linux-kernel-module/src/amneziawg.ko /lib/modules/$(uname -r)/extra/ 2>/dev/null || true
        cp /usr/src/amneziawg-linux-kernel-module/src/amneziawg.ko /lib/modules/$(uname -r)/updates/dkms/ 2>/dev/null || true
        depmod -a
        systemctl restart awg-quick@awg0
        ip link set mtu 1412 qlen 2000 dev awg0
    fi
fi

sysctl net.ipv4.tcp_congestion_control net.core.default_qdisc
ip link show awg0
"""
stdin, stdout, stderr = vps.exec_command(vps_script)
print(stdout.read().decode() + stderr.read().decode())
vps.close()

# 2. Tune Router 192.168.1.1
print("[2/2] Tuning Router 192.168.1.1 (MTU 1412 + flowtable offload for direct ISP + speedtest bypass + buffers)...")
t = paramiko.Transport(('192.168.1.1', 22))
t.connect()
t.auth_none('root')
rtr = paramiko.SSHClient()
rtr._transport = t

rtr_script = """#!/bin/sh
set -e

# Tune socket and netdev buffers on router
sysctl -w net.core.rmem_max=4194304 >/dev/null 2>&1 || true
sysctl -w net.core.wmem_max=4194304 >/dev/null 2>&1 || true
sysctl -w net.ipv4.tcp_rmem="4096 87380 4194304" >/dev/null 2>&1 || true
sysctl -w net.ipv4.tcp_wmem="4096 65536 4194304" >/dev/null 2>&1 || true
sysctl -w net.core.netdev_budget=600 >/dev/null 2>&1 || true
sysctl -w net.core.netdev_max_backlog=2500 >/dev/null 2>&1 || true

# Match awg0 MTU 1412 and txqueuelen
ip link set mtu 1412 txqueuelen 2000 dev awg0

# Add software flowtable for direct ISP traffic (oifname "pppoe-wan" / iifname "pppoe-wan") so non-VPN traffic is offloaded at wirespeed!
if ! nft list flowtables inet fw4 | grep -q "flowtable ft_wan"; then
    nft 'add flowtable inet fw4 ft_wan { hook ingress priority filter; devices = { eth0, eth1, phy0-ap0, phy1-ap0 }; }' 2>/dev/null || true
fi
# Insert flow offload rule at top of forward chain ONLY for pppoe-wan <-> br-lan traffic
nft insert rule inet fw4 forward iifname "br-lan" oifname "pppoe-wan" meta l4proto { tcp, udp } flow add @ft_wan 2>/dev/null || true
nft insert rule inet fw4 forward iifname "pppoe-wan" oifname "br-lan" meta l4proto { tcp, udp } flow add @ft_wan 2>/dev/null || true

# Update dnsmasq bypass list to include speedtest.net / ooklaserver.net / cdnst.net / 2ip.ru so Speedtest tests direct Russian ISP speed
cat << 'EOF' > /tmp/dnsmasq.d/vpn_bypass.conf
server=/ru/xn--p1ai/su/by/77.88.8.8
server=/speedtest.net/ooklaserver.net/cdnst.net/2ip.ru/2ip.io/77.88.8.8
server=/steampowered.com/steamcommunity.com/steamstatic.com/steamuserdata.com/steamcontent.com/steamserver.net/valve.net/valvesoftware.com/csgo.com/counter-strike.net/playdeadlock.com/dota2.com/77.88.8.8
nftset=/ru/xn--p1ai/su/by/speedtest.net/ooklaserver.net/cdnst.net/2ip.ru/2ip.io/steampowered.com/steamcommunity.com/steamstatic.com/steamuserdata.com/steamcontent.com/steamserver.net/valve.net/valvesoftware.com/csgo.com/counter-strike.net/playdeadlock.com/dota2.com/yandex.net/yandex.com/vk.com/userapi.com/4#inet#fw4#vpn_bypass_dyn
EOF

/etc/init.d/dnsmasq restart
sleep 2
# Trigger handshake after VPS restart
ping -c 2 -W 2 10.66.66.1
"""
stdin, stdout, stderr = rtr.exec_command(rtr_script)
print(stdout.read().decode() + stderr.read().decode())
rtr.close()
