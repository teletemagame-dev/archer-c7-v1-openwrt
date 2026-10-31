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
ip addr show
swconfig dev switch0 show | grep -A 10 "Port 1:"
logread | grep -E 'ppp|wan|netifd' | tail -n 25
"""
stdin, stdout, stderr = ssh.exec_command(cmd)
print(stdout.read().decode('utf-8', errors='replace') + stderr.read().decode('utf-8', errors='replace'))
ssh.close()
