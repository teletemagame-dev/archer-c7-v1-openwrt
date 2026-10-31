import paramiko

t = paramiko.Transport(('192.168.1.1', 22))
t.connect()
t.auth_none('root')
ssh = paramiko.SSHClient()
ssh._transport = t

cmd = """
sed -i 's/.*enable-ubus.*/\\t:/g' /etc/init.d/dnsmasq
sed -i 's/user=dnsmasq/user=root/g' /etc/init.d/dnsmasq
/etc/init.d/dnsmasq restart
sleep 2
ps | grep dnsmasq
netstat -ulpn | grep :53
"""
stdin, stdout, stderr = ssh.exec_command(cmd)
print(stdout.read().decode() + stderr.read().decode())
ssh.close()
