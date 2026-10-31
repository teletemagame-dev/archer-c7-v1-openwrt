import paramiko
import time

t = paramiko.Transport(('192.168.1.1', 22))
t.connect()
t.auth_none('root')
ssh = paramiko.SSHClient()
ssh._transport = t

def run_cmd(cmd):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    return stdout.read().decode('utf-8', errors='replace'), stderr.read().decode('utf-8', errors='replace')

# Let's check current mangle_prerouting and test conntrack mark (ct mark) optimization!
# How ct mark works:
# - Packet arrives on eth1.3 or wlan_vpn -> netdev ingress sets meta mark = 0x66
# - In mangle_prerouting:
#   1. If meta mark != 0x66 -> return (not from VPN port/SSID)
#   2. If udp/tcp dport 53 -> return (let dstnat redirect to local dnsmasq)
#   3. Fast path for already-classified connections (99.99% of all packets!):
#      - ct mark 0x66 -> return (keep meta mark 0x66 -> route via table 66 / awg0!)
#      - ct mark 0x99 -> meta mark set 0x0 return (bypass VPN -> route via main / pppoe-wan!)
#   4. Slow path ONLY for the 1st packet of a new connection (ct mark 0x0):
#      - ip daddr @vpn_bypass_static -> ct mark set 0x99 meta mark set 0x0 return
#      - ip daddr @vpn_bypass_dyn -> ct mark set 0x99 meta mark set 0x0 return
#      - udp dport { 3478, 4379-4380, 27000-27200 } -> ct mark set 0x99 meta mark set 0x0 return
#      - Default for new VPN connection: ct mark set 0x66 return

apply_fast_ct = """#!/bin/sh
set -e

# Enable packet steering (RPS) across queues and raise netdev budget for 100Mbps+ throughput
for rps in /sys/class/net/*/queues/rx-*/rps_cpus; do
    echo 1 > "$rps" 2>/dev/null || true
done
sysctl -w net.core.netdev_budget=600 >/dev/null 2>&1 || true
sysctl -w net.core.netdev_max_backlog=2000 >/dev/null 2>&1 || true

# Apply O(1) conntrack-cached mangle_prerouting
nft flush chain inet fw4 mangle_prerouting
nft add rule inet fw4 mangle_prerouting meta mark != 0x66 return
nft add rule inet fw4 mangle_prerouting udp dport 53 return
nft add rule inet fw4 mangle_prerouting tcp dport 53 return
nft add rule inet fw4 mangle_prerouting ct mark 0x66 return
nft add rule inet fw4 mangle_prerouting ct mark 0x99 meta mark set 0x0 return
nft add rule inet fw4 mangle_prerouting ip daddr @vpn_bypass_static ct mark set 0x99 meta mark set 0x0 return
nft add rule inet fw4 mangle_prerouting ip daddr @vpn_bypass_dyn ct mark set 0x99 meta mark set 0x0 return
nft add rule inet fw4 mangle_prerouting udp dport { 3478, 4379-4380, 27000-27200 } ct mark set 0x99 meta mark set 0x0 return
nft add rule inet fw4 mangle_prerouting ct mark set 0x66 return

# Also enable nftables flowtable offloading for bypassed (direct ISP pppoe-wan) flows!
# Notice: if ct mark == 0x99 (or ct mark == 0x0 from LAN 2-4 / teletema / ArcherC7v1-5G), offloading to @ft gives hardware-like wirespeed!
nft list chain inet fw4 mangle_prerouting
"""

out, err = run_cmd(apply_fast_ct)
print(out, err)
ssh.close()
