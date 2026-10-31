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

apply_script = """#!/bin/sh
set -e

# 1. Ensure routes for DNS servers through awg0
ip route replace 1.1.1.1/32 dev awg0
ip route replace 1.0.0.1/32 dev awg0

# 2. Configure dnsmasq to use VPS 10.66.66.1 as primary upstream, then 1.0.0.1, 1.1.1.1
uci delete dhcp.@dnsmasq[0].server 2>/dev/null || true
uci add_list dhcp.@dnsmasq[0].server='10.66.66.1'
uci add_list dhcp.@dnsmasq[0].server='1.0.0.1'
uci add_list dhcp.@dnsmasq[0].server='1.1.1.1'
uci set dhcp.@dnsmasq[0].strict_order='1'
uci commit dhcp

# 3. Update /tmp/dnsmasq.d/vpn_bypass.conf
cat << 'EOF' > /tmp/dnsmasq.d/vpn_bypass.conf
server=/ru/xn--p1ai/su/by/77.88.8.8
server=/speedtest.net/ooklaserver.net/cdnst.net/2ip.ru/2ip.io/77.88.8.8
server=/steampowered.com/steamcommunity.com/steamstatic.com/steamuserdata.com/steamcontent.com/steamserver.net/valve.net/valvesoftware.com/csgo.com/counter-strike.net/playdeadlock.com/dota2.com/77.88.8.8
nftset=/ru/xn--p1ai/su/by/speedtest.net/ooklaserver.net/cdnst.net/2ip.ru/2ip.io/steampowered.com/steamcommunity.com/steamstatic.com/steamuserdata.com/steamcontent.com/steamserver.net/valve.net/valvesoftware.com/csgo.com/counter-strike.net/playdeadlock.com/dota2.com/yandex.net/yandex.com/vk.com/userapi.com/4#inet#fw4#vpn_bypass_dyn
EOF

/etc/init.d/dnsmasq restart

# 4. Insert QUIC reject rule in forward chain if not present
if ! nft list chain inet fw4 forward | grep -q "udp dport 443 reject"; then
    nft insert rule inet fw4 forward meta mark 0x66 udp dport 443 reject with icmpx type port-unreachable
fi

# 5. Persist in /etc/amnezia/start_vpn.sh
sed -i 's/server=.1.0.0.1./server=\\'10.66.66.1\\'\\nuci add_list dhcp.@dnsmasq[0].server=\\'1.0.0.1\\'\\nuci add_list dhcp.@dnsmasq[0].server=\\'1.1.1.1\\'\\nuci set dhcp.@dnsmasq[0].strict_order=\\'1\\'/g' /etc/amnezia/start_vpn.sh 2>/dev/null || true
if ! grep -q "udp dport 443 reject" /etc/amnezia/start_vpn.sh; then
    sed -i '/nft add rule inet fw4 dstnat/i nft insert rule inet fw4 forward meta mark 0x66 udp dport 443 reject with icmpx type port-unreachable 2>/dev/null || true' /etc/amnezia/start_vpn.sh
fi
if ! grep -q "1.1.1.1/32 dev awg0" /etc/amnezia/start_vpn.sh; then
    sed -i '/ip route replace 1.0.0.1/i ip route replace 1.1.1.1/32 dev awg0 2>/dev/null || true' /etc/amnezia/start_vpn.sh
fi

echo "=== APPLIED SUCCESSFULLY ==="
cat /var/etc/dnsmasq.conf.* | grep -E 'server|strict'
"""

stdin, stdout, stderr = ssh.exec_command(apply_script)
print(stdout.read().decode('utf-8', errors='replace') + stderr.read().decode('utf-8', errors='replace'))
ssh.close()
