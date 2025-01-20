import subprocess

def run_exploit(module, rhost, rport, payload):
    print ("Running Metasploit. . .")
    try:
        command = f"msfconsole -q -x 'use {module}; set RHOST {rhost}; set RPORT {rport}; set payload {payload}; exploit'"
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"[-] Error running Metasploit: {e}")
        
