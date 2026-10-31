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
echo "=== FILTER AAAA IN DNSMASQ ==="
grep -i "filter-aaaa" /var/etc/dnsmasq.conf.*
echo "=== ICMP ERROR HANDLING / MTU ==="
sysctl net.ipv4.ip_no_pmtu_disc
cat /etc/config/dhcp | grep -E 'filter_aaaa|server'
echo "=== WAN IPV6 ==="
ip -6 addr show pppoe-wan 2>&1 || true
"""
stdin, stdout, stderr = ssh.exec_command(cmd)
print(stdout.read().decode('utf-8', errors='replace') + stderr.read().decode('utf-8', errors='replace'))
ssh.close()
