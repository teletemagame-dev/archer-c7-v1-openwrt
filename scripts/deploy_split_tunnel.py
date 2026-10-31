import paramiko
import os
import time

ROUTER_IP = '192.168.1.1'
NFT_GZ_LOCAL = r'./\output\vpn_bypass.nft.gz'

t = paramiko.Transport((ROUTER_IP, 22))
t.connect()
t.auth_none('root')
ssh = paramiko.SSHClient()
ssh._transport = t

def run_cmd(cmd):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    out = stdout.read().decode('utf-8', errors='replace')
    err = stderr.read().decode('utf-8', errors='replace')
    return out, err

def put_bytes(data, remote_path):
    stdin, stdout, stderr = ssh.exec_command(f"cat > {remote_path}")
    stdin.write(data)
    stdin.channel.shutdown_write()
    stdout.read()
    stderr.read()

print("[1/5] Uploading vpn_bypass.nft.gz...")
run_cmd("mkdir -p /etc/amnezia")
with open(NFT_GZ_LOCAL, "rb") as f:
    put_bytes(f.read(), "/etc/amnezia/vpn_bypass.nft.gz")

print("[2/5] Installing dnsmasq with nftset support...")
setup_dnsmasq = """#!/bin/sh
set -e
if [ -f /tmp/dnsmasq.new ]; then
    chmod +x /tmp/dnsmasq.new
    cp /tmp/dnsmasq.new /usr/sbin/dnsmasq
    rm -f /tmp/dnsmasq.new
fi

# Patch /etc/init.d/dnsmasq so it runs directly as root (needed for nftset netlink) and skips --enable-ubus
sed -i 's/procd_add_jail/#procd_add_jail/g' /etc/init.d/dnsmasq
sed -i 's/--enable-ubus//g' /etc/init.d/dnsmasq
"""
out, err = run_cmd(setup_dnsmasq)
if err:
    print("dnsmasq setup stderr:", err)

print("[3/5] Writing /etc/amnezia/start_vpn.sh...")
start_vpn_sh = """#!/bin/sh
# AmneziaWG + Split-Tunneling (LAN 1 + ArcherC7v1_VPN) Startup Script

export PATH="/usr/sbin:/usr/bin:/sbin:/bin"

# 1. Load kernel modules
for m in udp_tunnel ip6_udp_tunnel libcurve25519-generic chacha-mips poly1305-mips libchacha20poly1305 amneziawg; do
    if ! lsmod | grep -q "^${m}"; then
        insmod /lib/modules/5.15.167/${m}.ko 2>/dev/null || true
    fi
done

# 2. Ensure Switch Port 2 (Physical LAN 1) is on VLAN 3 (eth1.3) in br-lan
if ! ip link show eth1.3 >/dev/null 2>&1; then
    ip link add link eth1 name eth1.3 type vlan id 3 2>/dev/null || true
fi
ip link set eth1.3 master br-lan 2>/dev/null || true
ip link set eth1.3 up 2>/dev/null || true

uci set network.@switch_vlan[0].ports='3 4 5 0t'
if ! uci show network | grep -q "vlan='3'"; then
    v=$(uci add network switch_vlan)
    uci set network.${v}.device='switch0'
    uci set network.${v}.vlan='3'
    uci set network.${v}.ports='2 0t'
fi
uci set network.@device[0].ports='eth1.1 eth1.3'
uci commit network 2>/dev/null || true

swconfig dev switch0 vlan 3 set vid 3 2>/dev/null || true
swconfig dev switch0 vlan 3 set ports "0t 2" 2>/dev/null || true
swconfig dev switch0 vlan 1 set ports "0t 3 4 5" 2>/dev/null || true
swconfig dev switch0 port 2 set pvid 3 2>/dev/null || true
swconfig dev switch0 set apply 1 2>/dev/null || true

# 3. Ensure 3rd Wi-Fi AP (ArcherC7v1_VPN on 5GHz radio1) is configured and in br-lan
if ! uci -q get wireless.vpn_radio1 >/dev/null 2>&1; then
    uci set wireless.vpn_radio1=wifi-iface
    uci set wireless.vpn_radio1.device='radio1'
    uci set wireless.vpn_radio1.network='lan'
    uci set wireless.vpn_radio1.mode='ap'
    uci set wireless.vpn_radio1.ssid='ArcherC7v1_VPN'
    uci set wireless.vpn_radio1.encryption='psk2'
    uci set wireless.vpn_radio1.key='CHANGE_ME_VPN_WIFI_PASSWORD'
    uci set wireless.vpn_radio1.ifname='wlan_vpn'
    uci set wireless.vpn_radio1.disabled='0'
    uci commit wireless 2>/dev/null || true
    /sbin/wifi reload 2>/dev/null || true
    sleep 3
fi
ip link set wlan_vpn master br-lan 2>/dev/null || true

# 4. Bring up awg0 interface
if ! ip link show awg0 >/dev/null 2>&1; then
    ip link add dev awg0 type amneziawg
fi
awg setconf awg0 /etc/amnezia/awg0.conf
ip addr replace 10.66.66.2/24 dev awg0
ip link set mtu 1380 up dev awg0

sysctl -w net.ipv4.conf.all.rp_filter=0 >/dev/null 2>&1 || true
sysctl -w net.ipv4.conf.default.rp_filter=0 >/dev/null 2>&1 || true
sysctl -w net.ipv4.conf.awg0.rp_filter=0 >/dev/null 2>&1 || true

# 5. Update firewall config (disable flow_offloading for L3 tunnel compatibility, add awg0 to wan zone)
uci set firewall.@defaults[0].flow_offloading='0'
if ! uci -q get firewall.@zone[1].device | grep -q 'awg0'; then
    uci add_list firewall.@zone[1].device='awg0'
fi
uci commit firewall 2>/dev/null || true
/etc/init.d/firewall reload 2>/dev/null || true

# 6. Load static & dynamic bypass sets into table inet fw4
zcat /etc/amnezia/vpn_bypass.nft.gz | nft -f -
nft add element inet fw4 vpn_bypass_static { 203.0.113.1/32 } 2>/dev/null || true

# 7. Configure netdev ingress tagging on eth1.3 (LAN 1) and wlan_vpn (ArcherC7v1_VPN)
nft delete table netdev vpn_tag 2>/dev/null || true
nft add table netdev vpn_tag
nft 'add chain netdev vpn_tag ing_lan1 { type filter hook ingress device "eth1.3" priority -100; policy accept; meta mark set 0x66; }'
if ip link show wlan_vpn >/dev/null 2>&1; then
    nft 'add chain netdev vpn_tag ing_wifi { type filter hook ingress device "wlan_vpn" priority -100; policy accept; meta mark set 0x66; }'
fi

# 8. Configure fw4 dstnat (DNS interception for VPN ports) & mangle_prerouting (split-tunneling)
nft flush chain inet fw4 dstnat 2>/dev/null || true
nft add rule inet fw4 dstnat meta mark 0x66 udp dport 53 redirect to :53
nft add rule inet fw4 dstnat meta mark 0x66 tcp dport 53 redirect to :53

nft flush chain inet fw4 mangle_prerouting 2>/dev/null || true
nft add rule inet fw4 mangle_prerouting meta mark != 0x66 return
nft add rule inet fw4 mangle_prerouting udp dport 53 return
nft add rule inet fw4 mangle_prerouting tcp dport 53 return
nft add rule inet fw4 mangle_prerouting ip daddr @vpn_bypass_static meta mark set 0x0 return
nft add rule inet fw4 mangle_prerouting ip daddr @vpn_bypass_dyn meta mark set 0x0 return
nft add rule inet fw4 mangle_prerouting udp dport { 27000-27200, 3478, 4379-4380 } meta mark set 0x0 return

# 9. Configure policy routing (table 66 -> awg0) and encrypted DNS upstream (1.0.0.1 -> awg0)
ip route del 1.1.1.1/32 dev awg0 2>/dev/null || true
ip route replace 1.0.0.1/32 dev awg0
ip route replace 192.168.1.0/24 dev br-lan table 66
ip route replace default dev awg0 table 66
while ip rule del fwmark 0x66 lookup 66 2>/dev/null; do :; done
ip rule add fwmark 0x66 lookup 66 priority 100

# 10. Configure dnsmasq split-DNS & nftset auto-population
uci delete dhcp.@dnsmasq[0].server 2>/dev/null || true
uci add_list dhcp.@dnsmasq[0].server='1.0.0.1'
uci commit dhcp 2>/dev/null || true

mkdir -p /tmp/dnsmasq.d
cat << 'EOF' > /tmp/dnsmasq.d/vpn_bypass.conf
server=/ru/xn--p1ai/su/by/77.88.8.8
server=/steampowered.com/steamcommunity.com/steamstatic.com/steamuserdata.com/steamcontent.com/steamserver.net/valve.net/valvesoftware.com/csgo.com/counter-strike.net/playdeadlock.com/dota2.com/77.88.8.8
nftset=/ru/xn--p1ai/su/by/steampowered.com/steamcommunity.com/steamstatic.com/steamuserdata.com/steamcontent.com/steamserver.net/valve.net/valvesoftware.com/csgo.com/counter-strike.net/playdeadlock.com/dota2.com/yandex.net/yandex.com/vk.com/userapi.com/4#inet#fw4#vpn_bypass_dyn
EOF

/etc/init.d/dnsmasq restart 2>/dev/null || true
"""

put_bytes(start_vpn_sh.replace('\r\n', '\n').encode('utf-8'), "/etc/amnezia/start_vpn.sh")
run_cmd("chmod +x /etc/amnezia/start_vpn.sh")

print("[4/5] Updating /etc/rc.local and hotplug to persist across reboots & WAN reconnects...")
rc_local = """#!/bin/sh
# Ensure QCA9880-AR1A (hw1.0) 5GHz, 2.4GHz Wi-Fi, and AmneziaWG Split-Tunnel start on boot

(
    sysctl -w kernel.panic_on_oops=0 kernel.panic=0 >/dev/null 2>&1 || true
    sleep 15

    if ! lsmod | grep -q '^ath10k_pci'; then
        insmod /lib/modules/*/ath10k_core.ko 2>/dev/null || modprobe ath10k_core 2>/dev/null || true
        insmod /lib/modules/*/ath10k_pci.ko 2>/dev/null || modprobe ath10k_pci 2>/dev/null || true
        sleep 5
    fi

    if [ ! -d /sys/class/ieee80211/phy0 ] || [ ! -d /sys/class/ieee80211/phy1 ] || ! iwinfo | grep -qi 'ArcherC7v1-5G'; then
        /sbin/wifi config >/dev/null 2>&1 || true
        for r in radio0 radio1; do
            band=$(uci -q get wireless.${r}.band)
            if [ "$band" = "5g" ]; then
                uci set wireless.${r}.disabled='0'
                uci set wireless.${r}.country='US'
                uci set wireless.${r}.channel='36'
                uci set wireless.${r}.htmode='VHT80'
                uci set wireless.${r}.noscan='1'
                uci set wireless.default_${r}.ssid='ArcherC7v1-5G'
                uci set wireless.default_${r}.encryption='psk2'
                uci set wireless.default_${r}.key='CHANGE_ME_WIFI_PASSWORD'
                uci set wireless.default_${r}.disabled='0'
            elif [ "$band" = "2g" ]; then
                uci set wireless.${r}.disabled='0'
                uci set wireless.${r}.country='US'
                uci set wireless.${r}.channel='1'
                uci set wireless.${r}.htmode='HT20'
                uci set wireless.${r}.noscan='1'
                uci set wireless.default_${r}.ssid='ArcherC7v1-2G'
                uci set wireless.default_${r}.encryption='psk2'
                uci set wireless.default_${r}.key='CHANGE_ME_WIFI_PASSWORD'
                uci set wireless.default_${r}.disabled='0'
            fi
        done
        uci commit wireless >/dev/null 2>&1 || true
        /sbin/wifi reload >/dev/null 2>&1 || true
        sleep 5
    fi

    /etc/amnezia/start_vpn.sh >/tmp/amnezia_vpn.log 2>&1 || true
) &

exit 0
"""
put_bytes(rc_local.replace('\r\n', '\n').encode('utf-8'), "/etc/rc.local")
run_cmd("chmod +x /etc/rc.local")

hotplug_script = """#!/bin/sh
if [ "$ACTION" = "ifup" ] && [ "$INTERFACE" = "wan" ]; then
    /etc/amnezia/start_vpn.sh >/tmp/amnezia_vpn.log 2>&1 &
fi
"""
put_bytes(hotplug_script.replace('\r\n', '\n').encode('utf-8'), "/etc/hotplug.d/iface/99-amnezia-vpn")
run_cmd("chmod +x /etc/hotplug.d/iface/99-amnezia-vpn")

print("[5/5] Executing /etc/amnezia/start_vpn.sh...")
out, err = run_cmd("/etc/amnezia/start_vpn.sh 2>&1")
print(out)
if err:
    print("STDERR:", err)

out2, _ = run_cmd("awg show; ip rule show; ps | grep dnsmasq")
print("=== STATUS ===\n" + out2)

ssh.close()
