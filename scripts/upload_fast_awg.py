import paramiko

KO_LOCAL = r'./\output\amneziawg.ko'

t = paramiko.Transport(('192.168.1.1', 22))
t.connect()
t.auth_none('root')
ssh = paramiko.SSHClient()
ssh._transport = t

with open(KO_LOCAL, "rb") as f:
    data = f.read()

stdin, stdout, stderr = ssh.exec_command("cat > /lib/modules/5.15.167/amneziawg.ko")
stdin.write(data)
stdin.channel.shutdown_write()
stdout.read()

stdin, stdout, stderr = ssh.exec_command("""
ip link del awg0 2>/dev/null || true
rmmod amneziawg 2>/dev/null || true
insmod /lib/modules/5.15.167/amneziawg.ko
/etc/amnezia/start_vpn.sh
ping -c 2 -W 2 10.66.66.1
""")
print(stdout.read().decode() + stderr.read().decode())
ssh.close()
