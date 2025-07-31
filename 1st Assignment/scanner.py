import socket
import time
target = "scanme.nmap.org"
print(f"Scanning {target} (ports 1-100):\n")
for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port}: OPEN")
    else:
        print(f"[-] Port {port}: CLOSED")
    s.close()
    time.sleep(0.1)
