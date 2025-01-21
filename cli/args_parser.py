import argparse

def parse_arguments():
    """
    Parse command-line arguments for the penetration testing CLI tool.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="CLI tool for penetration testing")
    parser.add_argument("-s", "--shodan", help="Search for devices using Shodan", action="store_true")
    parser.add_argument("-S", "--scan", help="Scan a network for devices", action="store_true")
    parser.add_argument("-m", "--msf", help="Run an exploit using Metasploit", action="store_true")
    parser.add_argument("-c", "--connect", help="Connect to a remote server", action="store_true")
    return parser.parse_args()
