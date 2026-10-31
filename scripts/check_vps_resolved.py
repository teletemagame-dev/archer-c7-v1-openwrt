import paramiko

vps = paramiko.SSHClient()
vps.set_missing_host_key_policy(paramiko.AutoAddPolicy())
vps.connect('203.0.113.1', 22, 'root', 'YOUR_VPS_ROOT_PASSWORD', timeout=10)
stdin, stdout, stderr = vps.exec_command("""
systemctl --version
man systemd-resolved.service 2>&1 | grep -i "DNSStubListenerExtra" || echo "No DNSStubListenerExtra"
""")
print(stdout.read().decode())
vps.close()
