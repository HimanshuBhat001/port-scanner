# Intelligent Port Scanner

A lightweight but insightful port scanner built using Python.  
It detects open TCP ports, identifies associated services, and maps basic security risks.  
This project is ideal for learning socket programming, reconnaissance, and cybersecurity fundamentals.

---

## 🔍 Features

- Scans commonly used TCP ports
- Identifies associated services (FTP, SSH, HTTP, MySQL…)
- Provides security risk insight for known services
- Clean, readable terminal output
- Uses Python’s socket library (no external dependencies)

---

## 🛠 Installation

Ensure Python 3 is installed.

Clone the repository:

```bash
git clone https://github.com/HimanshuBhat001/intelligent-port-scanner
```

Navigate into the project:

```bash
cd intelligent-port-scanner
```

---

## ▶️ How to Run

Run the main script:

```bash
python src/port_scanner.py
```

Enter a target IP or domain (e.g., `scanme.nmap.org`).

---

## 📄 Sample Output

```
=== Intelligent Port Scanner ===

Scanning target: scanme.nmap.org

[OPEN]   Port  22 (SSH)   → Risk: Low (encrypted, secure access)
[OPEN]   Port  80 (HTTP)  → Risk: Medium (unencrypted traffic)
[CLOSED] Port 443
...

Scan complete.
```

More examples available in:

```
examples/sample_output.txt
`
