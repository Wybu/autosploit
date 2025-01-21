import argparse
from modules.shodan_search import shodan_search
from modules.scanner import scan
from modules.msf import run_exploit
from modules.socket_connection import create_connection

def main():
    parser = argparse.ArgumentParser(description="CLI tool for penetration testing")
    parser.add_argument("-s", "--shodan", help="Search for devices using Shodan", action="store_true")
    parser.add_argument("-S", "--scan", help="Scan a network for devices", action="store_true")
    parser.add_argument("-m", "--msf", help="Run an exploit using Metasploit", action="store_true")
    parser.add_argument("-c", "--connect", help="Connect to a remote server", action="store_true")
    args = parser.parse_args()

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
