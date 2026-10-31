import paramiko
import socket
import time

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
echo "=== DNSMASQ CONFIG ==="
cat /var/etc/dnsmasq.conf.*
echo "=== DNSMASQ DROP-IN ==="
cat /tmp/dnsmasq.d/* 2>/dev/null
echo "=== FW4 MANGLE FORWARD ==="
nft list chain inet fw4 mangle_forward
echo "=== TEST DNS RESOLUTION TIMES FROM ROUTER ==="
time nslookup instagram.com 127.0.0.1
time nslookup youtube.com 127.0.0.1
time nslookup twitter.com 127.0.0.1
echo "=== PING 1.0.0.1 via awg0 ==="
ping -c 3 1.0.0.1
"""
stdin, stdout, stderr = ssh.exec_command(cmd)
print(stdout.read().decode('utf-8', errors='replace') + stderr.read().decode('utf-8', errors='replace'))
ssh.close()
