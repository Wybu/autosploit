import socket
import threading
import argparse
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

def scan(target, start_port, end_port):
    """
    Quét các cổng từ start_port đến end_port trên mục tiêu.
    """
    target_ip = socket.gethostbyname(target)
    print(f"Scanning {target_ip}...")
    for port in range(start_port, end_port + 1):
        scan_port(target_ip, port)

def parse_arguments():
   
    parser = argparse.ArgumentParser(description="Port scanner")
    parser.add_argument("target", help="Target domain or IP address to scan")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port range (default: 1)")
    parser.add_argument("-e", "--end", type=int, default=1024, help="End port range (default: 1024)")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    scan(args.target, args.start, args.end)
