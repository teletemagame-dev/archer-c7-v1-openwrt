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
logread | grep -E 'ppp|PAD|LCP' | tail -n 25
echo "--- Restarting WAN ---"
ifup wan
sleep 6
ip addr show pppoe-wan
logread | grep -E 'ppp|PAD|LCP' | tail -n 15
"""
stdin, stdout, stderr = ssh.exec_command(cmd)
print(stdout.read().decode('utf-8', errors='replace') + stderr.read().decode('utf-8', errors='replace'))
ssh.close()
