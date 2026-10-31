import paramiko

# 1. Check VPS 203.0.113.1 sysctl, bbr, mtu, interface speed
vps = paramiko.SSHClient()
vps.set_missing_host_key_policy(paramiko.AutoAddPolicy())
vps.connect('10.66.66.1', 22, 'root', 'YOUR_VPS_ROOT_PASSWORD', timeout=10)
stdin, stdout, stderr = vps.exec_command("""
sysctl net.ipv4.tcp_congestion_control net.core.default_qdisc
ip link show awg0
ethtool eth0 2>/dev/null || ethtool ens3 2>/dev/null || true
tc qdisc show
""")
print("=== VPS 203.0.113.1 ===")
print(stdout.read().decode())
vps.close()

# 2. Check Router 192.168.1.1 cpuinfo, network offloads, qdisc
t = paramiko.Transport(('192.168.1.1', 22))
t.connect()
t.auth_none('root')
rtr = paramiko.SSHClient()
rtr._transport = t
stdin, stdout, stderr = rtr.exec_command("""
cat /proc/cpuinfo
ethtool -k eth0 2>/dev/null || true
ip link show eth0 eth0.2 pppoe-wan awg0 br-lan eth1 eth1.3
cat /proc/interrupts
""")
print("=== ROUTER 192.168.1.1 ===")
print(stdout.read().decode())
rtr.close()
