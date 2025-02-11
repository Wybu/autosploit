import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.shodan_search import shodan_search
from modules.scanner import scan
from modules.msf import run_exploit
from modules.socket_connection import create_connection
from cli.args_parser import parse_arguments  

def main():
    args = parse_arguments()  
    if args.shodan:
        shodan_search()
    elif args.scan:
        scan()
    elif args.msf:
        run_exploit()
    elif args.connect:
        create_connection()
    else:
        print("No arguments provided")

if __name__ == "__main__":
    main()
