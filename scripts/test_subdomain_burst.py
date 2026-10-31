import socket
import time

subdomains = [
    "www.youtube.com",
    "i.ytimg.com",
    "yt3.ggpht.com",
    "accounts.google.com",
    "play.google.com",
    "fonts.googleapis.com",
    "fonts.gstatic.com",
    "static.xx.fbcdn.net",
    "scontent.cdninstagram.com",
    "instagram.com",
    "graph.instagram.com",
    "edge-chat.instagram.com",
    "api.twitter.com",
    "pbs.twimg.com",
    "abs.twimg.com",
    "t.co",
    "chatgpt.com",
    "oaistatic.com",
    "oaiusercontent.com",
    "cdn.oaistatic.com"
]

t0 = time.time()
for s in subdomains:
    t_start = time.time()
    try:
        ip = socket.gethostbyname(s)
        dt = (time.time() - t_start) * 1000
        print(f"  {s:<30} -> {ip:<16} ({dt:5.1f} ms)")
    except Exception as e:
        dt = (time.time() - t_start) * 1000
        print(f"  {s:<30} -> FAILED: {e} ({dt:5.1f} ms)")

print(f"Total time for 20 queries: {(time.time() - t0)*1000:.1f} ms")
