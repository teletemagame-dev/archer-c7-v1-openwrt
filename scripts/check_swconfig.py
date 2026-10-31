import paramiko

t = paramiko.Transport(('192.168.1.1', 22))
t.connect()
t.auth_none('root')
ssh = paramiko.SSHClient()
ssh._transport = t

stdin, stdout, stderr = ssh.exec_command("swconfig dev switch0 show")
print(stdout.read().decode())
ssh.close()
