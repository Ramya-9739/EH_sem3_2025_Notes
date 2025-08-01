# EH_sem3_2025_Notes
# Assignment 19: Python Socket Port Scanner  
**Student ID:** Ramya-9739  

## 🧠 Methodology  
I wrote a 15-line Python script using the `socket` module to scan ports 1–100 on the domain `scanme.nmap.org`. The script attempts a TCP connection to each port and prints whether it is open or closed. A short sleep delay is added between scans using `time.sleep(0.1)`.

## 📸 Screenshot  
*(Insert `scan_output.png` in this directory)*
<img width="523" height="616" alt="image" src="https://github.com/user-attachments/assets/ea182e19-a455-457d-9d59-c26ccf4fa4bb" />


## 🔍 Findings  
- **Open ports found:** 22, 80 *(example — replace with your actual results)*
- Most ports were reported as closed, which is expected from secure servers.
- The scanner correctly identified port status using raw socket connections.

## 📘 Conclusion  
This assignment helped me understand how port scanning works using low-level Python socket programming. Unlike tools like Nmap that provide advanced scanning and service detection, this script helped me learn how basic connection attempts can reveal open ports.

## 🧑‍💻 Code  

```python
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
