import paramiko

# 1. Patch VPS amneziawg.ko in /root/amneziawg-linux-kernel-module/src/socket.c so outer UDP checksum is 0 (saves MIPS RX CPU)
vps = paramiko.SSHClient()
vps.set_missing_host_key_policy(paramiko.AutoAddPolicy())
vps.connect('10.66.66.1', 22, 'root', 'YOUR_VPS_ROOT_PASSWORD', timeout=10)
stdin, stdout, stderr = vps.exec_command("""
for d in /root/amneziawg-linux-kernel-module/src /usr/src/amneziawg*/src; do
    if [ -f "$d/socket.c" ]; then
        echo "Found $d/socket.c"
        if grep -q "fl.fl4_dport, false, false" "$d/socket.c"; then
            sed -i 's/fl.fl4_dport, false, false/fl.fl4_dport, false, true/g' "$d/socket.c"
            make -C /lib/modules/$(uname -r)/build M="$d" -j$(nproc) modules
            make -C /lib/modules/$(uname -r)/build M="$d" modules_install
            depmod -a
            nohup bash -c 'sleep 1; systemctl restart awg-quick@awg0; ip link set mtu 1412 qlen 2000 dev awg0' >/dev/null 2>&1 &
        fi
        break
    fi
done
""")
print(stdout.read().decode() + stderr.read().decode())
vps.close()

# 2. Apply router part cleanly
t = paramiko.Transport(('192.168.1.1', 22))
t.connect()
t.auth_none('root')
rtr = paramiko.SSHClient()
rtr._transport = t

rtr_script = """#!/bin/sh
set -e
ip link set mtu 1412 qlen 2000 dev awg0

if ! nft list flowtables inet fw4 | grep -q "flowtable ft_wan"; then
    nft 'add flowtable inet fw4 ft_wan { hook ingress priority filter; devices = { eth0, eth1, phy0-ap0, phy1-ap0 }; }' 2>/dev/null || true
fi
if ! nft list chain inet fw4 forward | grep -q "flow add @ft_wan"; then
    nft insert rule inet fw4 forward iifname "br-lan" oifname "pppoe-wan" meta l4proto { tcp, udp } flow add @ft_wan 2>/dev/null || true
    nft insert rule inet fw4 forward iifname "pppoe-wan" oifname "br-lan" meta l4proto { tcp, udp } flow add @ft_wan 2>/dev/null || true
fi

cat << 'EOF' > /tmp/dnsmasq.d/vpn_bypass.conf
server=/ru/xn--p1ai/su/by/77.88.8.8
server=/speedtest.net/ooklaserver.net/cdnst.net/2ip.ru/2ip.io/77.88.8.8
server=/steampowered.com/steamcommunity.com/steamstatic.com/steamuserdata.com/steamcontent.com/steamserver.net/valve.net/valvesoftware.com/csgo.com/counter-strike.net/playdeadlock.com/dota2.com/77.88.8.8
nftset=/ru/xn--p1ai/su/by/speedtest.net/ooklaserver.net/cdnst.net/2ip.ru/2ip.io/steampowered.com/steamcommunity.com/steamstatic.com/steamuserdata.com/steamcontent.com/steamserver.net/valve.net/valvesoftware.com/csgo.com/counter-strike.net/playdeadlock.com/dota2.com/yandex.net/yandex.com/vk.com/userapi.com/4#inet#fw4#vpn_bypass_dyn
EOF

/etc/init.d/dnsmasq restart
sleep 3
awg setconf awg0 /etc/amnezia/awg0.conf
ping -c 2 -W 2 10.66.66.1
"""
stdin, stdout, stderr = rtr.exec_command(rtr_script)
print(stdout.read().decode() + stderr.read().decode())
rtr.close()
