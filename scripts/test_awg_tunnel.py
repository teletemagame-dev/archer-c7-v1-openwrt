#!/usr/bin/env python3
import socket
import paramiko

AWG_CONF = """[Interface]
PrivateKey = YOUR_AWG_CLIENT_PRIVATE_KEY_BASE64=
Jc = 4
Jmin = 40
Jmax = 70
S1 = 44
S2 = 96
H1 = 1320987123
H2 = 1784329011
H3 = 2049182736
H4 = 1592837465

[Peer]
PublicKey = YOUR_AWG_SERVER_PUBLIC_KEY_BASE64=
PresharedKey = YOUR_AWG_PRESHARED_KEY_BASE64=
Endpoint = 203.0.113.1:51820
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
"""

s = socket.create_connection(("192.168.1.1", 22), timeout=5)
t = paramiko.Transport(s)
t.start_client()
t.auth_none("root")


def run_ssh(cmd, data=None):
    ch = t.open_session()
    ch.exec_command(cmd)
    if data is not None:
        ch.sendall(data)
        ch.shutdown_write()
    res = b""
    while True:
        d = ch.recv(4096)
        if not d:
            break
        res += d
    ch.close()
    return res.decode("utf-8", "ignore")


run_ssh("mkdir -p /etc/amnezia && cat > /etc/amnezia/awg0.conf && chmod 600 /etc/amnezia/awg0.conf", AWG_CONF.encode("utf-8"))
out = run_ssh("""
ip link del dev awg0 2>/dev/null || true
ip link add dev awg0 type amneziawg
/usr/bin/awg setconf awg0 /etc/amnezia/awg0.conf
ip addr add 10.66.66.2/24 dev awg0
ip link set mtu 1412 up dev awg0
ping -c 3 -W 3 10.66.66.1
/usr/bin/awg show awg0
""")
print(out)
t.close()
