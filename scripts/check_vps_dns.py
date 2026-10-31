import paramiko

vps = paramiko.SSHClient()
vps.set_missing_host_key_policy(paramiko.AutoAddPolicy())
vps.connect('203.0.113.1', 22, 'root', 'YOUR_VPS_ROOT_PASSWORD', timeout=10)
stdin, stdout, stderr = vps.exec_command("""
ss -tulpn | grep :53
cat /etc/resolv.conf
resolvectl status 2>/dev/null || systemd-resolve --status 2>/dev/null || true
""")
print(stdout.read().decode() + stderr.read().decode())
vps.close()
