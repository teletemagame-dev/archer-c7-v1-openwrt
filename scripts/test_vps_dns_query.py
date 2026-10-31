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
time nslookup instagram.com 10.66.66.1
time nslookup twitter.com 10.66.66.1
time nslookup youtube.com 10.66.66.1
time nslookup instagram.com 10.66.66.1
"""
stdin, stdout, stderr = ssh.exec_command(cmd)
print(stdout.read().decode() + stderr.read().decode())
ssh.close()
