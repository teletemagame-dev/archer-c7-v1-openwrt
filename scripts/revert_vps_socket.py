import paramiko

vps = paramiko.SSHClient()
vps.set_missing_host_key_policy(paramiko.AutoAddPolicy())
vps.connect('203.0.113.1', 22, 'root', 'YOUR_VPS_ROOT_PASSWORD', timeout=10)
stdin, stdout, stderr = vps.exec_command("""
for d in /root/amneziawg-linux-kernel-module/src /usr/src/amneziawg*/src; do
    if [ -f "$d/socket.c" ]; then
        sed -i 's/fl.fl4_dport, false, true/fl.fl4_dport, false, false/g' "$d/socket.c"
        make -C /lib/modules/$(uname -r)/build M="$d" -j$(nproc) modules
        cp "$d/amneziawg.ko" /lib/modules/$(uname -r)/extra/ 2>/dev/null || true
        cp "$d/amneziawg.ko" /lib/modules/$(uname -r)/updates/dkms/ 2>/dev/null || true
        depmod -a
        systemctl stop awg-quick@awg0
        rmmod amneziawg 2>/dev/null || true
        modprobe amneziawg
        systemctl start awg-quick@awg0
        ip link set mtu 1412 qlen 2000 dev awg0
        break
    fi
done
awg show
""")
print(stdout.read().decode('utf-8', errors='replace') + stderr.read().decode('utf-8', errors='replace'))
vps.close()
