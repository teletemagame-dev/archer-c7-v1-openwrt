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

# 1. Update UCI DHCP cleanly
run_cmd("""
uci delete dhcp.@dnsmasq[0].server 2>/dev/null || true
uci add_list dhcp.@dnsmasq[0].server='10.66.66.1'
uci add_list dhcp.@dnsmasq[0].server='1.0.0.1'
uci add_list dhcp.@dnsmasq[0].server='1.1.1.1'
uci set dhcp.@dnsmasq[0].strict_order='1'
uci commit dhcp
/etc/init.d/dnsmasq restart
ip route replace 1.1.1.1/32 dev awg0
ip route replace 1.0.0.1/32 dev awg0
if ! nft list chain inet fw4 forward | grep -q "udp dport 443 reject"; then
    nft insert rule inet fw4 forward meta mark 0x66 udp dport 443 reject with icmpx type port-unreachable
fi
""")

out, _ = run_cmd("""
echo "=== DNSMASQ CONFIG ==="
cat /var/etc/dnsmasq.conf.* | grep -E 'server|strict'
echo "=== FW4 FORWARD ==="
nft list chain inet fw4 forward | head -n 6
echo "=== ROUTES ==="
ip route show | grep -E '1.1.1.1|1.0.0.1'
""")
print(out)
ssh.close()
