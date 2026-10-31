import paramiko
import time

t = paramiko.Transport(('192.168.1.1', 22))
t.connect()
t.auth_none('root')
ssh = paramiko.SSHClient()
ssh._transport = t

script = """#!/bin/sh
set -e

# 1. Create eth1.3 and attach to br-lan seamlessly before moving Switch Port 2 (LAN 1) to VLAN 3
if ! ip link show eth1.3 >/dev/null 2>&1; then
    ip link add link eth1 name eth1.3 type vlan id 3
fi
ip link set eth1.3 master br-lan
ip link set eth1.3 up

# Update switch0 in UCI
uci set network.@switch_vlan[0].ports='3 4 5 0t'
if ! uci show network | grep -q "vlan='3'"; then
    v=$(uci add network switch_vlan)
    uci set network.${v}.device='switch0'
    uci set network.${v}.vlan='3'
    uci set network.${v}.ports='2 0t'
fi
uci set network.@device[0].ports='eth1.1 eth1.3'
uci commit network

# Apply switch0 VLAN 3 live without resetting PHYs
swconfig dev switch0 vlan 3 set vid 3
swconfig dev switch0 vlan 3 set ports "0t 2"
swconfig dev switch0 vlan 1 set ports "0t 3 4 5"
swconfig dev switch0 port 2 set pvid 3
swconfig dev switch0 set apply 1

# 2. Configure 3rd Wi-Fi network ArcherC7v1_VPN on 5GHz (radio1)
uci set wireless.vpn_radio1=wifi-iface
uci set wireless.vpn_radio1.device='radio1'
uci set wireless.vpn_radio1.network='lan'
uci set wireless.vpn_radio1.mode='ap'
uci set wireless.vpn_radio1.ssid='ArcherC7v1_VPN'
uci set wireless.vpn_radio1.encryption='psk2'
uci set wireless.vpn_radio1.key='CHANGE_ME_VPN_WIFI_PASSWORD'
uci set wireless.vpn_radio1.ifname='wlan_vpn'
uci set wireless.vpn_radio1.disabled='0'
uci commit wireless

/sbin/wifi reload
sleep 4
iwinfo
brctl show 2>/dev/null || bridge link
swconfig dev switch0 show | tail -n 35
"""

stdin, stdout, stderr = ssh.exec_command(script)
print(stdout.read().decode('utf-8', errors='replace'))
print(stderr.read().decode('utf-8', errors='replace'))
ssh.close()
