import paramiko

t = paramiko.Transport(('192.168.1.1', 22))
t.connect()
t.auth_none('root')
ssh = paramiko.SSHClient()
ssh._transport = t

cmd = """
ip route get 1.0.0.1
nslookup google.com 1.0.0.1 2>&1
nslookup playdeadlock.com 1.0.0.1 2>&1
nslookup playdeadlock.com 77.88.8.8 2>&1
"""
stdin, stdout, stderr = ssh.exec_command(cmd)
print(stdout.read().decode() + stderr.read().decode())
ssh.close()
