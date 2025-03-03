import socket  # Import the socket module for network connections

# Function to scan a single port
def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
        s.settimeout(1)  # Set a timeout for the connection attempt
        result = s.connect_ex((ip, port))  # Try connecting to the target IP and port
        if result == 0:  # If connection is successful (returns 0), the port is open
            print(f"Port {port} is open")
        s.close()  # Close the socket after checking
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

# Function to scan multiple ports in a range
def scan_ports(ip, start_port, end_port):
    print(f"Scanning {ip} for open ports...")
    for port in range(start_port, end_port + 1):  # Loop through the given port range
        scan_port(ip, port)  # Call the function to scan each port

# Example usage
#target_ip = "192.168.1.1"  # Replace with the target IP address
#scan_ports(target_ip, 1, 1024)  # Scan ports from 1 to 1024

target_ip=input("Enter the target ip address: ")
start_port=int(input("Enter start port: "))
end_port= int(input("Enter end port: "))
scan_ports(target_ip, start_port, end_port)