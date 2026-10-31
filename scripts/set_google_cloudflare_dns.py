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

def run_cmd(cmd):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    return stdout.read().decode('utf-8', errors='replace'), stderr.read().decode('utf-8', errors='replace')

# 1. Update upstream DNS in UCI to Cloudflare (1.1.1.1, 1.0.0.1) and Google (8.8.8.8, 8.8.4.4)
run_cmd("""
uci delete dhcp.@dnsmasq[0].server 2>/dev/null || true
uci add_list dhcp.@dnsmasq[0].server='1.1.1.1'
uci add_list dhcp.@dnsmasq[0].server='8.8.8.8'
uci add_list dhcp.@dnsmasq[0].server='1.0.0.1'
uci add_list dhcp.@dnsmasq[0].server='8.8.4.4'
uci set dhcp.@dnsmasq[0].strict_order='0'

# Update DHCP option 6 on LAN to Cloudflare & Google
uci delete dhcp.lan.dhcp_option 2>/dev/null || true
uci add_list dhcp.lan.dhcp_option='6,1.1.1.1,8.8.8.8,1.0.0.1,8.8.4.4'
uci commit dhcp
""")

# 2. Update /tmp/dnsmasq.d/vpn_bypass.conf to REMOVE speedtest.net so Speedtest runs through VPN!
# Also clean up @vpn_bypass_dyn in nftables
run_cmd("""
cat << 'EOF' > /tmp/dnsmasq.d/vpn_bypass.conf
server=/ru/xn--p1ai/su/by/77.88.8.8
server=/steampowered.com/steamcommunity.com/steamstatic.com/steamuserdata.com/steamcontent.com/steamserver.net/valve.net/valvesoftware.com/csgo.com/counter-strike.net/playdeadlock.com/dota2.com/77.88.8.8
nftset=/ru/xn--p1ai/su/by/steampowered.com/steamcommunity.com/steamstatic.com/steamuserdata.com/steamcontent.com/steamserver.net/valve.net/valvesoftware.com/csgo.com/counter-strike.net/playdeadlock.com/dota2.com/yandex.net/yandex.com/vk.com/userapi.com/4#inet#fw4#vpn_bypass_dyn
EOF

# Flush dynamic set and any cached speedtest elements
nft flush set inet fw4 vpn_bypass_dyn 2>/dev/null || true

# Route Cloudflare and Google DNS via awg0
ip route replace 1.1.1.1/32 dev awg0
ip route replace 1.0.0.1/32 dev awg0
ip route replace 8.8.8.8/32 dev awg0
ip route replace 8.8.4.4/32 dev awg0

/etc/init.d/dnsmasq restart
""")

# 3. Persist these settings in /etc/amnezia/start_vpn.sh
stdin, stdout, stderr = ssh.exec_command("cat /etc/amnezia/start_vpn.sh")
sh_content = stdout.read().decode('utf-8')

# Replace DNS section in start_vpn.sh
old_part = "uci delete dhcp.@dnsmasq[0].server"
new_dns_block = """uci delete dhcp.@dnsmasq[0].server 2>/dev/null || true
uci add_list dhcp.@dnsmasq[0].server='1.1.1.1'
uci add_list dhcp.@dnsmasq[0].server='8.8.8.8'
uci add_list dhcp.@dnsmasq[0].server='1.0.0.1'
uci add_list dhcp.@dnsmasq[0].server='8.8.4.4'
uci set dhcp.@dnsmasq[0].strict_order='0'
uci delete dhcp.lan.dhcp_option 2>/dev/null || true
uci add_list dhcp.lan.dhcp_option='6,1.1.1.1,8.8.8.8,1.0.0.1,8.8.4.4'
uci commit dhcp 2>/dev/null || true

mkdir -p /tmp/dnsmasq.d
cat << 'EOF' > /tmp/dnsmasq.d/vpn_bypass.conf
server=/ru/xn--p1ai/su/by/77.88.8.8
server=/steampowered.com/steamcommunity.com/steamstatic.com/steamuserdata.com/steamcontent.com/steamserver.net/valve.net/valvesoftware.com/csgo.com/counter-strike.net/playdeadlock.com/dota2.com/77.88.8.8
nftset=/ru/xn--p1ai/su/by/steampowered.com/steamcommunity.com/steamstatic.com/steamuserdata.com/steamcontent.com/steamserver.net/valve.net/valvesoftware.com/csgo.com/counter-strike.net/playdeadlock.com/dota2.com/yandex.net/yandex.com/vk.com/userapi.com/4#inet#fw4#vpn_bypass_dyn
EOF

/etc/init.d/dnsmasq restart 2>/dev/null || true
"""

# Also ensure DNS routes in start_vpn.sh
new_routes = """ip route replace 1.1.1.1/32 dev awg0 2>/dev/null || true
ip route replace 1.0.0.1/32 dev awg0 2>/dev/null || true
ip route replace 8.8.8.8/32 dev awg0 2>/dev/null || true
ip route replace 8.8.4.4/32 dev awg0 2>/dev/null || true"""

import re
sh_content = re.sub(r'ip route replace 1\.1\.1\.1.*?dev awg0.*?\n', '', sh_content)
sh_content = re.sub(r'ip route replace 1\.0\.0\.1.*?dev awg0.*?\n', '', sh_content)
sh_content = sh_content.replace('ip route replace default dev awg0 table 66', f'ip route replace default dev awg0 table 66\n{new_routes}')

# Replace the dnsmasq block in start_vpn.sh
if "mkdir -p /tmp/dnsmasq.d" in sh_content:
    sh_content = re.sub(r'uci delete dhcp.@dnsmasq\[0\].server.*?(?=/etc/init.d/dnsmasq restart.*?\n)/etc/init.d/dnsmasq restart 2>/dev/null \|\| true',
                        new_dns_block.strip(), sh_content, flags=re.DOTALL)

stdin, stdout, stderr = ssh.exec_command("cat > /etc/amnezia/start_vpn.sh")
stdin.write(sh_content)
stdin.channel.shutdown_write()
stdout.read()

out, _ = run_cmd("""
echo "=== DNSMASQ CONFIG ==="
cat /var/etc/dnsmasq.conf.* | grep -E 'server|strict'
echo "=== ROUTES ==="
ip route show | grep dev\\ awg0
echo "=== BYPASS CONF ==="
cat /tmp/dnsmasq.d/vpn_bypass.conf
""")
print(out)
ssh.close()
