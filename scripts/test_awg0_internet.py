import paramiko

t = paramiko.Transport(('192.168.1.1', 22))
t.connect()
t.auth_none('root')
ssh = paramiko.SSHClient()
ssh._transport = t

cmd = """
ping -c 2 -W 2 10.66.66.1
ip route replace 1.1.1.1/32 dev awg0
ping -c 2 -W 2 1.1.1.1
wget -qO- --timeout=5 http://api.ipify.org 2>&1 || true
"""
stdin, stdout, stderr = ssh.exec_command(cmd)
print(stdout.read().decode() + stderr.read().decode())
ssh.close()
