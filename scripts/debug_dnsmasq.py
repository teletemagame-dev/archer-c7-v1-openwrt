import paramiko

t = paramiko.Transport(('192.168.1.1', 22))
t.connect()
t.auth_none('root')
ssh = paramiko.SSHClient()
ssh._transport = t

cmd = """
ls -la /var/etc/dnsmasq*
cat /var/etc/dnsmasq.conf.*
/usr/sbin/dnsmasq -C /var/etc/dnsmasq.conf.cfg01411c --test 2>&1 || true
"""
stdin, stdout, stderr = ssh.exec_command(cmd)
print(stdout.read().decode() + stderr.read().decode())
ssh.close()
