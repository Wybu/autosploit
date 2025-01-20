import socket

def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))
        
def create_connection(ip, port):
    try:
        print(f"[+] Đang kết nối đến {ip}:{port}")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        print("[+] Kết nối thành công!")
        return s
    except Exception as e:
        print(f"[-] Không thể kết nối: {e}")
        return None    