import nmap  # Import the nmap module for scanning

# Function to perform an Nmap scan
def nmap_scan(target_ip, scan_type):
    scanner = nmap.PortScanner()  # Initialize the Nmap scanner object
    print(f"Scanning {target_ip} with {scan_type} scan...")

    if scan_type == "syn":
        scanner.scan(target_ip, "1-1024", "-sS")  # Perform a SYN scan (-sS)
    elif scan_type == "tcp":
        scanner.scan(target_ip, "1-1024", "-sT")  # Perform a TCP connect scan (-sT)
    elif scan_type == "udp":
        scanner.scan(target_ip, "1-1024", "-sU")  # Perform a UDP scan (-sU)
    elif scan_type == "os":
        scanner.scan(target_ip, arguments="-O")  # Perform OS detection (-O)
    elif scan_type == "all":
        scanner.scan(target_ip, "1-1024", "-sS -sU -O -A")  # Perform a full scan
    else:
        print("Invalid scan type. Choose syn, tcp, udp, os, or all.")
        return

    for host in scanner.all_hosts():  # Iterate over detected hosts
        print(f"\nHost: {host} ({scanner[host].hostname()})")
        print(f"State: {scanner[host].state()}")

        for proto in scanner[host].all_protocols():  # Loop through detected protocols
            print(f"\nProtocol: {proto}")
            ports = scanner[host][proto].keys()  # Get scanned ports
            for port in ports:
                print(f"Port {port}: {scanner[host][proto][port]['state']}")

# Example usage
target = "192.168.1.1"  # Replace with the target IP address
nmap_scan(target, "syn")  # Perform a SYN scan
