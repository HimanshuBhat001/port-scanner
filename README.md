# Advanced Port Scanner

A fast, multithreaded port-scanning tool built in Python.  
This project scans common TCP ports and identifies open ports on a target IP/Domain.  
Useful for ethical hacking practice, cybersecurity learning, and network analysis.

---

## ⚡ Features

- Fast multithreaded scanning  
- Scans first 1024 common TCP ports  
- Clean and readable output  
- Error-handling for closed/filtered ports  
- Lightweight (uses only Python standard libraries)  

---

## 🛠 Installation

Ensure Python 3 is installed.

Clone the repository:

```bash
git clone https://github.com/HimanshuBhat001/advanced-port-scanner
```

Navigate into the project:

```bash
cd advanced-port-scanner
```

---

## ▶️ How to Run

```bash
python src/port_scanner.py
```

Enter a target like:

```
scanme.nmap.org
```
or  
```
192.168.1.10
```

---

## 📄 Sample Output

```
Scanning target: scanme.nmap.org
----------------------------------------
[OPEN] Port 22
[OPEN] Port 80

Scan complete.
```
## 🧠 Project Structure

```
advanced-port-scanner/
│
├── src/
│   └── port_scanner.py
│
├── docs/
│   └── overview.md
│
├── examples/
│   └── sample_output.txt
│   └── .keep
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## 📘 Documentation

See the technical overview in:

```
docs/overview.md
```

Covers:
- TCP scanning basics  
- Socket programming  
- Threading model  
- Limitations of simple scanners  

---

## 🚀 Future Enhancements

- UDP port scanning  
- Banner grabbing  
- Advanced scan modes (SYN, FIN, Xmas)  
- Async-based scanner (super fast)  
- HTML logging of scan results  

---

## 👤 Author

**Himanshu Bhat**  
Cybersecurity | Python | Cloud | Networking  

---

## 📄 License

Licensed under the **MIT License**.
