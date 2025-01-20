#port scanner
import socket
import threading
from queue import Queue

print_lock = threading.Lock()
