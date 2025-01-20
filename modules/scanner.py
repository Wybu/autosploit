#port scanner
import socket
import threading
from queue import Queue

print_lock = threading.Lock()

def scan_port(target_ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        con = s.connect((target_ip, port))
        with print_lock:
            print(f"[+] Port {port} is open")
        con.close()
    except:
        pass
    
def scan(target):
    target_ip = socket.gethostbyname(target)
    print(f"Scanning {target_ip}")
    for port in range(1, 1025):
        scan_port(target_ip, port)
    
