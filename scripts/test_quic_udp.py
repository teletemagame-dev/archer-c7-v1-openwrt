import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(2.0)
s.bind(('192.168.1.110', 0))
# Send a dummy QUIC Initial packet (1200 bytes)
quic_probe = b'\xc0\x00\x00\x00\x01' + b'\x00'*1200
t0 = time.time()
try:
    s.sendto(quic_probe, ('157.240.196.174', 443)) # instagram
    data, addr = s.recvfrom(2048)
    print("QUIC UDP response:", len(data), "bytes")
except Exception as e:
    print(f"QUIC probe timeout or error after {time.time()-t0:.2f}s: {e}")
finally:
    s.close()
