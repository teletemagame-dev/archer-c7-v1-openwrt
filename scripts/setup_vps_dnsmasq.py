import paramiko

vps = paramiko.SSHClient()
vps.set_missing_host_key_policy(paramiko.AutoAddPolicy())
vps.connect('203.0.113.1', 22, 'root', 'YOUR_VPS_ROOT_PASSWORD', timeout=10)
stdin, stdout, stderr = vps.exec_command("""
apt-get update -qq && apt-get install -y -qq dnsmasq
cat << 'EOF' > /etc/dnsmasq.d/awg.conf
interface=awg0
bind-interfaces
listen-address=10.66.66.1
server=1.1.1.1
server=1.0.0.1
server=8.8.8.8
cache-size=10000
no-resolv
EOF
systemctl restart dnsmasq
sleep 1
ss -tulpn | grep :53
""")
print(stdout.read().decode() + stderr.read().decode())
vps.close()
