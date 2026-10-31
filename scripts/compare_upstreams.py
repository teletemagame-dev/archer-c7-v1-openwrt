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
for srv in 77.88.8.8 8.8.8.8 1.0.0.1; do
    echo "--- Server $srv ---"
    for domain in instagram.com twitter.com rutracker.org linkedin.com t.me youtube.com discord.com; do
        ans=$(nslookup $domain $srv 2>&1 | grep -A 2 "Non-authoritative" | tail -n 2)
        echo "  $domain: $ans"
    done
done
"""
stdin, stdout, stderr = ssh.exec_command(cmd)
print(stdout.read().decode('utf-8', errors='replace') + stderr.read().decode('utf-8', errors='replace'))
ssh.close()
