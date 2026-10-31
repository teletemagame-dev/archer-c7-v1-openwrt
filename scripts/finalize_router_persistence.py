import paramiko

t = paramiko.Transport(('192.168.1.1', 22))
t.connect()
t.auth_none('root')
ssh = paramiko.SSHClient()
ssh._transport = t

def run_cmd(cmd):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    return stdout.read().decode('utf-8', errors='replace'), stderr.read().decode('utf-8', errors='replace')

def put_bytes(data, remote_path):
    stdin, stdout, stderr = ssh.exec_command(f"cat > {remote_path}")
    stdin.write(data)
    stdin.channel.shutdown_write()
    stdout.read()
    stderr.read()

watchdog_sh = """#!/bin/sh
# AmneziaWG Watchdog: ensures awg0 handshake and policy routing stay healthy 24/7
export PATH="/usr/sbin:/usr/bin:/sbin:/bin"

while true; do
    sleep 45
    if ! ip link show awg0 >/dev/null 2>&1 || ! ip rule show | grep -q "fwmark 0x66 lookup 66"; then
        /etc/amnezia/start_vpn.sh >/tmp/amnezia_vpn.log 2>&1 || true
        continue
    fi
    if ! ping -c 1 -W 3 -I awg0 10.66.66.1 >/dev/null 2>&1; then
        if ! ping -c 1 -W 3 -I awg0 10.66.66.1 >/dev/null 2>&1; then
            awg setconf awg0 /etc/amnezia/awg0.conf 2>/dev/null || true
            ping -c 1 -W 3 -I awg0 10.66.66.1 >/dev/null 2>&1 || true
        fi
    fi
done
"""

put_bytes(watchdog_sh.replace('\r\n', '\n').encode('utf-8'), "/etc/amnezia/watchdog.sh")
run_cmd("chmod +x /etc/amnezia/watchdog.sh")

# Ensure watchdog is in /etc/rc.local and running once
run_cmd("grep -q watchdog.sh /etc/rc.local || sed -i 's|start_vpn.sh.*|start_vpn.sh >/tmp/amnezia_vpn.log 2>\\&1 || true; /etc/amnezia/watchdog.sh >/dev/null 2>\\&1 \\&|' /etc/rc.local")
run_cmd("killall watchdog.sh 2>/dev/null || true; /etc/amnezia/watchdog.sh >/dev/null 2>&1 &")

# Verify everything on router
out, err = run_cmd("""
iwinfo | grep -E 'ESSID|Channel|Tx-Power'
echo "---"
swconfig dev switch0 show | tail -n 12
echo "---"
awg show
echo "---"
ip rule show
echo "---"
ps | grep -E 'dnsmasq|watchdog'
""")
print(out)
ssh.close()
