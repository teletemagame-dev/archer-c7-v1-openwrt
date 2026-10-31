import paramiko

t = paramiko.Transport(('192.168.1.1', 22))
t.connect()
t.auth_none('root')
ssh = paramiko.SSHClient()
ssh._transport = t

cmd = """
nft add table netdev test_in 2>&1
nft 'add chain netdev test_in ing { type filter hook ingress device "lo" priority 0; policy accept; meta mark set 0x100; }' 2>&1
nft list table netdev test_in 2>&1
nft delete table netdev test_in 2>&1
"""
stdin, stdout, stderr = ssh.exec_command(cmd)
print(stdout.read().decode() + stderr.read().decode())
ssh.close()
