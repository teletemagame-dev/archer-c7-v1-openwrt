import urllib.request
import re

try:
    resp = urllib.request.urlopen("http://192.168.0.1/", timeout=3)
    html = resp.read().decode('utf-8', errors='replace')
    print("Old router HTTP 200, title / content preview:")
    title = re.search(r'<title>(.*?)</title>', html, re.I)
    print("Title:", title.group(1) if title else "No title")
    print("Preview:\n", html[:500])
except Exception as e:
    print("Error querying 192.168.0.1:", e)
