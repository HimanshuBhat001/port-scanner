# Technical Overview – Intelligent Port Scanner

This port scanner evaluates a host by testing common TCP ports and mapping each to the expected service. Along with detection, it associates known security risk levels with specific services.

---

## How It Works

### 1. Socket-based Port Scanning
The scanner:
- Creates a TCP socket
- Attempts a connection to a port
- If connection succeeds → Port is open
- If it fails → Port is closed or filtered

### 2. Service Identification
Each port is matched to:
- FTP, SSH, Telnet, HTTP, HTTPS, SMB, MySQL, RDP…

### 3. Risk Mapping
Services have well-known risks:
- HTTP = unencrypted  
- Telnet = insecure  
- FTP = plaintext  
- SSH = secure  

The scanner uses a lookup table to display these insights.

---

## Limitations

- TCP-only (no UDP scanning)
- No multithreading (current version = simple)
- Can be slow on high-latency networks
- No banner grabbing or advanced fingerprinting

---

## Future Developments

- Threaded version for faster scanning
- SYN scan mode (requires raw sockets)
- OS fingerprinting add-on
- Export results to JSON / HTML
