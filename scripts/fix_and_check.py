import paramiko

t = paramiko.Transport(('192.168.1.1', 22))
t.connect()
t.auth_none('root')
ssh = paramiko.SSHClient()
ssh._transport = t

cmd = """
nft delete table netdev vpn_tag 2>/dev/null || true
nft flush chain inet fw4 mangle_prerouting 2>/dev/null || true
ip rule show
ip route show table 66 2>/dev/null || true
ip addr show awg0 2>/dev/null || true
"""
stdin, stdout, stderr = ssh.exec_command(cmd)
print(stdout.read().decode() + stderr.read().decode())
ssh.close()
