import paramiko
import socket
import time

print("Sending reboot command to Archer C7 v1...")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5.0)
sock.bind(('192.168.1.110', 0))
sock.connect(('192.168.1.1', 22))
t = paramiko.Transport(sock)
t.connect()
t.auth_none('root')
ssh = paramiko.SSHClient()
ssh._transport = t
try:
    ssh.exec_command("/sbin/reboot")
except Exception:
    pass
ssh.close()

print("Reboot issued! Waiting ~40-45 seconds for router to boot up...")
time.sleep(30)

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)
        s.bind(('192.168.1.110', 0))
        s.connect(('192.168.1.1', 22))
        t = paramiko.Transport(s)
        t.connect()
        t.auth_none('root')
        ssh = paramiko.SSHClient()
        ssh._transport = t
        print("Connected to 192.168.1.1! Waiting for rc.local (sleep 25) to complete...")
        time.sleep(12)
        stdin, stdout, stderr = ssh.exec_command("iwinfo; awg show; ip rule show")
        out = stdout.read().decode('utf-8', errors='replace')
        print("=== ROUTER STATUS AFTER REBOOT ===\n" + out)
        ssh.close()
        break
    except Exception as e:
        time.sleep(3)
