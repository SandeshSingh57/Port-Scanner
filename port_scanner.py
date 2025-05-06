import socket

def scan_ports(target_ip, start_port, end_port):
    print(f"\nScanning {target_ip} from port {start_port} to {end_port}...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)  
            result = s.connect_ex((target_ip, port))  
            if result == 0:
                print(f" Port {port} is OPEN")
                open_ports.append(port)
            s.close()
        except socket.error:
            print(f" Couldn't connect to port {port}")
    
    if not open_ports:
        print("No open ports found in the given range.")
    else:
        print(f"\nTotal open ports: {len(open_ports)}")

def validate_ip(ip):
    parts = ip.strip().split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        n = int(part)
        if n < 0 or n > 255:
            return False
    return True

if __name__ == "__main__":
    print(" Basic Port Scanner \n")
    
    ip = input("Enter the IP address to scan: ").strip()
    if not validate_ip(ip):
        print(" Invalid IP address format.")
        exit()

    try:
        start = int(input("Enter start port (e.g. 20): "))
        end = int(input("Enter end port (e.g. 80): "))

        if start < 1 or end > 65535 or start > end:
            raise ValueError

        scan_ports(ip, start, end)

    except ValueError:
        print("Invalid port range. Enter numbers between 1 and 65535.")
