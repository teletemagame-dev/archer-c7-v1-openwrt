import paramiko

def run_cmd(ssh, cmd):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    out = stdout.read().decode('utf-8', errors='replace')
    err = stderr.read().decode('utf-8', errors='replace')
    return out, err

t = paramiko.Transport(('192.168.1.1', 22))
t.connect()
t.auth_none('root')
ssh = paramiko.SSHClient()
ssh._transport = t

cmds = [
    "nft add table netdev test_in 2>&1; nft list tables; nft delete table netdev test_in 2>/dev/null",
    "nft add table bridge test_br 2>&1; nft list tables; nft delete table bridge test_br 2>/dev/null",
    "ls -la /lib/modules/5.15.167/*nft* /lib/modules/5.15.167/*bridge* 2>&1",
    "uci show network",
    "uci show wireless"
]

for c in cmds:
    out, err = run_cmd(ssh, c)
    print(f"=== {c} ===\n{out}{err}")

ssh.close()
