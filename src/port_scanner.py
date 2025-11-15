import socket

# Common ports and services
port_services = {
    20: "FTP-Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP"
}

# Basic security risk mapping
risk_levels = {
    "FTP": "High (unencrypted protocol)",
    "Telnet": "High (very insecure)",
    "HTTP": "Medium (unencrypted)",
    "SSH": "Low (secure encrypted access)",
    "HTTPS": "Low (secure encrypted protocol)",
    "MySQL": "Medium (database exposure risks)"
}

def scan_port(ip, port):
    s = socket.socket()
    s.settimeout(0.5)
    try:
        s.connect((ip, port))
        return True
    except:
        return False

target = input("Enter target IP: ")
print(f"\nScanning {target}...\n")

for port, service in port_services.items():
    if scan_port(target, port):
        risk = risk_levels.get(service, "Varies (depends on configuration)")
        print(f"[OPEN] Port {port} ({service}) → Risk: {risk}")
    else:
        print(f"[CLOSED] Port {port}")
