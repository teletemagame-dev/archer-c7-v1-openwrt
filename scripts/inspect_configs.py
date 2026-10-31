import paramiko

t = paramiko.Transport(('192.168.1.1', 22))
t.connect()
t.auth_none('root')
ssh = paramiko.SSHClient()
ssh._transport = t

for f in ["/etc/config/firewall", "/etc/config/dhcp", "/etc/rc.local"]:
    stdin, stdout, stderr = ssh.exec_command(f"cat {f}")
    print(f"=== {f} ===\n" + stdout.read().decode())

ssh.close()
