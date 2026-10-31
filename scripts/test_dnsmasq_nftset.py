import paramiko

t = paramiko.Transport(('192.168.1.1', 22))
t.connect()
t.auth_none('root')
ssh = paramiko.SSHClient()
ssh._transport = t

cmd = """
nslookup store.steampowered.com 127.0.0.1
nslookup api.steampowered.com 127.0.0.1
nslookup playdeadlock.com 127.0.0.1
nslookup ya.ru 127.0.0.1
nft list set inet fw4 vpn_bypass_dyn
logread | grep dnsmasq | tail -n 20
"""
stdin, stdout, stderr = ssh.exec_command(cmd)
print(stdout.read().decode() + stderr.read().decode())
ssh.close()
