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

stdin, stdout, stderr = ssh.exec_command("cat /etc/amnezia/start_vpn.sh")
content = stdout.read().decode('utf-8')

# Ensure 10.66.66.1, 1.0.0.1, 1.1.1.1 in start_vpn.sh
content = content.replace("uci add_list dhcp.@dnsmasq[0].server='77.88.8.8'", "# 77.88.8.8 used only for .ru")
content = content.replace("uci add_list dhcp.@dnsmasq[0].server='8.8.8.8'", "uci add_list dhcp.@dnsmasq[0].server='1.1.1.1'")
if "10.66.66.1" not in content:
    content = content.replace("uci add_list dhcp.@dnsmasq[0].server='1.0.0.1'", "uci add_list dhcp.@dnsmasq[0].server='10.66.66.1'\nuci add_list dhcp.@dnsmasq[0].server='1.0.0.1'")

if "strict_order" not in content:
    content = content.replace("uci commit dhcp", "uci set dhcp.@dnsmasq[0].strict_order='1'\nuci commit dhcp")

if "udp dport 443 reject" not in content:
    content = content.replace("nft add rule inet fw4 dstnat meta mark 0x66 udp dport 53 redirect to :53",
                              "nft insert rule inet fw4 forward meta mark 0x66 udp dport 443 reject with icmpx type port-unreachable 2>/dev/null || true\nnft add rule inet fw4 dstnat meta mark 0x66 udp dport 53 redirect to :53")

if "1.1.1.1/32 dev awg0" not in content:
    content = content.replace("ip route replace 1.0.0.1/32 dev awg0", "ip route replace 1.1.1.1/32 dev awg0\nip route replace 1.0.0.1/32 dev awg0")

stdin, stdout, stderr = ssh.exec_command("cat > /etc/amnezia/start_vpn.sh")
stdin.write(content)
stdin.channel.shutdown_write()
stdout.read()

stdin, stdout, stderr = ssh.exec_command("grep -E '10.66.66.1|strict_order|443 reject' /etc/amnezia/start_vpn.sh")
print("=== PERSISTENCE CHECK ===")
print(stdout.read().decode())
ssh.close()
