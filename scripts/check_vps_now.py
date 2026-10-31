import paramiko

vps = paramiko.SSHClient()
vps.set_missing_host_key_policy(paramiko.AutoAddPolicy())
vps.connect('203.0.113.1', 22, 'root', 'YOUR_VPS_ROOT_PASSWORD', timeout=10)
stdin, stdout, stderr = vps.exec_command("""
awg show
ip addr show awg0
systemctl status awg-quick@awg0 --no-pager -l
dmesg | tail -n 20
""")
print(stdout.read().decode() + stderr.read().decode())
vps.close()
