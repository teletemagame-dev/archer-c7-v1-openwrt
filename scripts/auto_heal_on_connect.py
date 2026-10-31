import paramiko
import time
import socket
import subprocess
import gzip
import re

KO_LOCAL = r'./\output\amneziawg.ko'
with open(KO_LOCAL, "rb") as f:
    KO_GZ_BYTES = gzip.compress(f.read(), compresslevel=9)

print(f"Prepared amneziawg.ko.gz ({len(KO_GZ_BYTES)/1024:.1f} KB)")

start_vpn_sh = """#!/bin/sh
# AmneziaWG + Fail-Open Backup Split-Tunneling (LAN 1 + ArcherC7v1_VPN)
export PATH="/usr/sbin:/usr/bin:/sbin:/bin"

# Prevent concurrent execution
if ! mkdir /var/run/amnezia_start.lock 2>/dev/null; then
    exit 0
fi
trap 'rmdir /var/run/amnezia_start.lock 2>/dev/null' EXIT INT TERM

# Always start in Fail-Open state (direct ISP internet active) until tunnel is verified
while ip rule del fwmark 0x66 lookup 66 2>/dev/null; do :; done
ip route del 1.0.0.1/32 dev awg0 2>/dev/null || true

# 1. Load kernel modules (decompress amneziawg.ko.gz into RAM /tmp to save flash space)
for m in udp_tunnel ip6_udp_tunnel libcurve25519-generic chacha-mips poly1305-mips libchacha20poly1305; do
    if ! lsmod | grep -q "^$(echo $m | tr '-' '_')"; then
        insmod /lib/modules/5.15.167/${m}.ko 2>/dev/null || true
    fi
done
if ! lsmod | grep -q "^amneziawg"; then
    if [ -f /etc/amnezia/amneziawg.ko.gz ]; then
        zcat /etc/amnezia/amneziawg.ko.gz > /tmp/amneziawg.ko && insmod /tmp/amneziawg.ko 2>/dev/null || true
        rm -f /tmp/amneziawg.ko
    elif [ -f /lib/modules/5.15.167/amneziawg.ko ]; then
        insmod /lib/modules/5.15.167/amneziawg.ko 2>/dev/null || true
    fi
fi

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

# 4. Configure dnsmasq split-DNS & nftset auto-population
cp /rom/etc/init.d/dnsmasq /etc/init.d/dnsmasq
sed -i '/--enable-ubus/d' /etc/init.d/dnsmasq
sed -i 's/procd_add_jail/true #/g' /etc/init.d/dnsmasq
sed -i 's/user=dnsmasq/user=root/g' /etc/init.d/dnsmasq

uci delete dhcp.@dnsmasq[0].server 2>/dev/null || true
uci add_list dhcp.@dnsmasq[0].server='1.0.0.1'
uci add_list dhcp.@dnsmasq[0].server='8.8.8.8'
uci add_list dhcp.@dnsmasq[0].server='77.88.8.8'
uci commit dhcp 2>/dev/null || true

mkdir -p /tmp/dnsmasq.d
cat << 'EOF' > /tmp/dnsmasq.d/vpn_bypass.conf
server=/ru/xn--p1ai/su/by/77.88.8.8
server=/speedtest.net/ooklaserver.net/cdnst.net/2ip.ru/2ip.io/77.88.8.8
server=/steampowered.com/steamcommunity.com/steamstatic.com/steamuserdata.com/steamcontent.com/steamserver.net/valve.net/valvesoftware.com/csgo.com/counter-strike.net/playdeadlock.com/dota2.com/77.88.8.8
nftset=/ru/xn--p1ai/su/by/speedtest.net/ooklaserver.net/cdnst.net/2ip.ru/2ip.io/steampowered.com/steamcommunity.com/steamstatic.com/steamuserdata.com/steamcontent.com/steamserver.net/valve.net/valvesoftware.com/csgo.com/counter-strike.net/playdeadlock.com/dota2.com/yandex.net/yandex.com/vk.com/userapi.com/4#inet#fw4#vpn_bypass_dyn
EOF

/etc/init.d/dnsmasq restart 2>/dev/null || true

# 5. Update firewall config & enable flowtable offload for direct ISP (pppoe-wan)
uci set firewall.@defaults[0].flow_offloading='0'
if ! uci -q get firewall.@zone[1].device | grep -q 'awg0'; then
    uci add_list firewall.@zone[1].device='awg0'
fi
uci commit firewall 2>/dev/null || true
/etc/init.d/firewall reload 2>/dev/null || true

if ! nft list flowtables | grep -q "flowtable ft_wan"; then
    nft 'add flowtable inet fw4 ft_wan { hook ingress priority filter; devices = { eth0, eth1, phy0-ap0, phy1-ap0 }; }' 2>/dev/null || true
fi
if ! nft list chain inet fw4 forward | grep -q "flow add @ft_wan"; then
    nft insert rule inet fw4 forward iifname "br-lan" oifname "pppoe-wan" meta l4proto { tcp, udp } flow add @ft_wan 2>/dev/null || true
    nft insert rule inet fw4 forward iifname "pppoe-wan" oifname "br-lan" meta l4proto { tcp, udp } flow add @ft_wan 2>/dev/null || true
fi

# 6. Load static & dynamic bypass sets into table inet fw4 (only if not already loaded)
if ! nft list sets inet fw4 | grep -q "vpn_bypass_static"; then
    zcat /etc/amnezia/vpn_bypass.nft.gz | nft -f -
fi

# 7. Configure netdev ingress tagging on eth1.3 (LAN 1) and wlan_vpn (ArcherC7v1_VPN)
nft delete table netdev vpn_tag 2>/dev/null || true
nft add table netdev vpn_tag
nft 'add chain netdev vpn_tag ing_lan1 { type filter hook ingress device "eth1.3" priority -100; policy accept; meta mark set 0x66; }'
if ip link show wlan_vpn >/dev/null 2>&1; then
    nft 'add chain netdev vpn_tag ing_wifi { type filter hook ingress device "wlan_vpn" priority -100; policy accept; meta mark set 0x66; }'
fi

# 8. Configure fw4 dstnat & O(1) conntrack-cached mangle_prerouting
nft flush chain inet fw4 dstnat 2>/dev/null || true
nft add rule inet fw4 dstnat meta mark 0x66 udp dport 53 redirect to :53
nft add rule inet fw4 dstnat meta mark 0x66 tcp dport 53 redirect to :53

nft flush chain inet fw4 mangle_prerouting 2>/dev/null || true
nft add rule inet fw4 mangle_prerouting meta mark != 0x66 return
nft add rule inet fw4 mangle_prerouting udp dport 53 return
nft add rule inet fw4 mangle_prerouting tcp dport 53 return
nft add rule inet fw4 mangle_prerouting ct mark 0x66 return
nft add rule inet fw4 mangle_prerouting ct mark 0x99 meta mark set 0x0 return
nft add rule inet fw4 mangle_prerouting ip daddr @vpn_bypass_static ct mark set 0x99 meta mark set 0x0 return
nft add rule inet fw4 mangle_prerouting ip daddr @vpn_bypass_dyn ct mark set 0x99 meta mark set 0x0 return
nft add rule inet fw4 mangle_prerouting udp dport { 3478, 4379-4380, 27000-27200 } ct mark set 0x99 meta mark set 0x0 return
nft add rule inet fw4 mangle_prerouting ct mark set 0x66 return

# 9. Bring up awg0 interface and VERIFY handshake before enabling policy routing (Fail-Open Guarantee!)
if ! ip link show awg0 >/dev/null 2>&1; then
    ip link add dev awg0 type amneziawg 2>/dev/null || true
fi
if ip link show awg0 >/dev/null 2>&1; then
    awg setconf awg0 /etc/amnezia/awg0.conf 2>/dev/null || true
    ip addr replace 10.66.66.2/24 dev awg0 2>/dev/null || true
    ip link set mtu 1412 qlen 2000 up dev awg0 2>/dev/null || true

    sysctl -w net.ipv4.conf.all.rp_filter=0 >/dev/null 2>&1 || true
    sysctl -w net.ipv4.conf.default.rp_filter=0 >/dev/null 2>&1 || true
    sysctl -w net.ipv4.conf.awg0.rp_filter=0 >/dev/null 2>&1 || true
    sysctl -w net.core.rmem_max=4194304 >/dev/null 2>&1 || true
    sysctl -w net.core.wmem_max=4194304 >/dev/null 2>&1 || true
    sysctl -w net.core.netdev_budget=600 >/dev/null 2>&1 || true
    sysctl -w net.core.netdev_max_backlog=2500 >/dev/null 2>&1 || true

    ip route replace 192.168.1.0/24 dev br-lan table 66 2>/dev/null || true
    ip route replace default dev awg0 table 66 2>/dev/null || true

    if ping -c 2 -W 2 -I awg0 10.66.66.1 >/dev/null 2>&1; then
        ip route replace 1.0.0.1/32 dev awg0 2>/dev/null || true
        ip rule add fwmark 0x66 lookup 66 priority 100 2>/dev/null || true
        logger -t amnezia "VPN tunnel awg0 UP and verified (10.66.66.1 reachable) -> VPN routing enabled"
    else
        logger -t amnezia "VPN tunnel awg0 unreachable -> FAIL-OPEN BACKUP ACTIVE (direct ISP internet)"
    fi
fi
"""

watchdog_sh = """#!/bin/sh
# AmneziaWG Fail-Open Watchdog (Single-Instance Lock)
export PATH="/usr/sbin:/usr/bin:/sbin:/bin"

if ! mkdir /var/run/amnezia_watchdog.lock 2>/dev/null; then
    exit 0
fi
trap 'rmdir /var/run/amnezia_watchdog.lock 2>/dev/null' EXIT INT TERM

while true; do
    sleep 12
    # If awg0 doesn't exist yet, try lightweight creation without reloading firewall/nftsets
    if ! ip link show awg0 >/dev/null 2>&1; then
        while ip rule del fwmark 0x66 lookup 66 2>/dev/null; do :; done
        ip route del 1.0.0.1/32 dev awg0 2>/dev/null || true
        if ! lsmod | grep -q "^amneziawg" && [ -f /etc/amnezia/amneziawg.ko.gz ]; then
            zcat /etc/amnezia/amneziawg.ko.gz > /tmp/amneziawg.ko && insmod /tmp/amneziawg.ko 2>/dev/null || true
            rm -f /tmp/amneziawg.ko
        fi
        ip link add dev awg0 type amneziawg 2>/dev/null || true
        awg setconf awg0 /etc/amnezia/awg0.conf 2>/dev/null || true
        ip addr replace 10.66.66.2/24 dev awg0 2>/dev/null || true
        ip link set mtu 1412 qlen 2000 up dev awg0 2>/dev/null || true
    fi

    # Only test tunnel if WAN (pppoe-wan) is up
    if ! ip addr show pppoe-wan 2>/dev/null | grep -q "inet "; then
        while ip rule del fwmark 0x66 lookup 66 2>/dev/null; do :; done
        ip route del 1.0.0.1/32 dev awg0 2>/dev/null || true
        continue
    fi

    if ping -c 1 -W 2 -I awg0 10.66.66.1 >/dev/null 2>&1 || ping -c 1 -W 2 -I awg0 10.66.66.1 >/dev/null 2>&1; then
        if ! ip rule show | grep -q "fwmark 0x66 lookup 66"; then
            ip route replace 192.168.1.0/24 dev br-lan table 66 2>/dev/null || true
            ip route replace default dev awg0 table 66 2>/dev/null || true
            ip route replace 1.0.0.1/32 dev awg0 2>/dev/null || true
            ip rule add fwmark 0x66 lookup 66 priority 100 2>/dev/null || true
            logger -t amnezia "Watchdog: VPN tunnel restored -> enabled VPN routing"
        fi
    else
        if ip rule show | grep -q "fwmark 0x66 lookup 66"; then
            while ip rule del fwmark 0x66 lookup 66 2>/dev/null; do :; done
            ip route del 1.0.0.1/32 dev awg0 2>/dev/null || true
            logger -t amnezia "Watchdog: VPN tunnel down -> FAIL-OPEN BACKUP activated (direct ISP internet)"
        fi
        awg setconf awg0 /etc/amnezia/awg0.conf 2>/dev/null || true
    fi
done
"""

def get_lan1_ip():
    out = subprocess.check_output("ipconfig", shell=True).decode('cp866', errors='replace')
    m = re.search(r'192\.168\.1\.(\d+)', out)
    if m and m.group(1) != '1':
        return f"192.168.1.{m.group(1)}"
    return None

print("Waiting for PC Ethernet to get 192.168.1.x from Archer C7 v1...")
while True:
    local_ip = get_lan1_ip()
    if not local_ip:
        time.sleep(1)
        continue
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3.0)
        sock.bind((local_ip, 0))
        sock.connect(('192.168.1.1', 22))
        t = paramiko.Transport(sock)
        t.connect()
        t.auth_none('root')
        ssh = paramiko.SSHClient()
        ssh._transport = t
        print(f"Connected to 192.168.1.1 from {local_ip}! Cleaning up and applying Fail-Open config...")

        def run_cmd(cmd):
            stdin, stdout, stderr = ssh.exec_command(cmd)
            return stdout.read().decode('utf-8', errors='replace'), stderr.read().decode('utf-8', errors='replace')

        def put_bytes(data, remote_path):
            stdin, stdout, stderr = ssh.exec_command(f"cat > {remote_path}")
            stdin.write(data)
            stdin.channel.shutdown_write()
            stdout.read()
            stderr.read()

        # 1. Kill any duplicate watchdog/start_vpn processes & clear lockfiles
        run_cmd("""
        for pid in $(ps | grep -E 'watchdog\\.sh|start_vpn\\.sh' | grep -v grep | awk '{print $1}'); do
            kill -9 $pid 2>/dev/null || true
        done
        rmdir /var/run/amnezia_start.lock /var/run/amnezia_watchdog.lock 2>/dev/null || true
        while ip rule del fwmark 0x66 lookup 66 2>/dev/null; do :; done
        ip route del 1.0.0.1/32 dev awg0 2>/dev/null || true
        rm -f /lib/modules/5.15.167/amneziawg.ko
        """)

        # 2. Upload compact 47KB gzipped amneziawg.ko.gz
        put_bytes(KO_GZ_BYTES, "/etc/amnezia/amneziawg.ko.gz")

        # 3. Upload lock-protected Fail-Open start_vpn.sh and watchdog.sh
        put_bytes(start_vpn_sh.replace('\r\n', '\n').encode('utf-8'), "/etc/amnezia/start_vpn.sh")
        put_bytes(watchdog_sh.replace('\r\n', '\n').encode('utf-8'), "/etc/amnezia/watchdog.sh")
        run_cmd("chmod +x /etc/amnezia/start_vpn.sh /etc/amnezia/watchdog.sh")

        # 4. Run start_vpn.sh and launch single watchdog.sh
        out, err = run_cmd("/etc/amnezia/start_vpn.sh; /etc/amnezia/watchdog.sh >/dev/null 2>&1 &")
        print(out, err)

        out2, _ = run_cmd("df -h /overlay; ps | grep -E 'dnsmasq|watchdog'; awg show; ip rule show")
        print("=== VERIFICATION ===\n" + out2)
        ssh.close()
        break
    except Exception as e:
        time.sleep(1)
