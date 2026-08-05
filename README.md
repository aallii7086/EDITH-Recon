
> **Enhanced Digital Intelligence for Threat Hunting**

A modular Python-based reconnaissance toolkit for DNS analysis, network enumeration, SSL inspection, subdomain enumeration, and automated report generation.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Kali_Linux-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-v1.1.0-orange)

---

## 📖 Project Overview

**EDITH Recon** is a modular reconnaissance toolkit developed in Python to automate the information gathering phase of security assessments.

It performs DNS resolution, Reverse DNS lookup, WHOIS enumeration, TCP port scanning, HTTP banner grabbing, SSL certificate inspection, and subdomain enumeration. The toolkit also generates professional TXT and HTML reports for every completed scan.

The project was built with a modular architecture, making it easy to maintain, extend, and integrate with future reconnaissance modules.
---

## ✨ Features

- 🌐 DNS Lookup
- 🔄 Reverse DNS Lookup
- 📄 WHOIS Lookup
- 🚪 Nmap Port Scanning
- 📡 HTTP Banner Grabbing
- 🔒 SSL Certificate Inspection
- 🌍 Subdomain Enumeration
- 🎯 Deep Scan (All Subdomains)
- 🔍 Deep Scan (Specific Subdomain)
- 📄 TXT Report Generation
- 🌐 HTML Report Generation
- 🧩 Modular Architecture
  
  ---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Core Programming Language |
| socket | Networking & Banner Grabbing |
| python-whois | WHOIS Lookup |
| python-nmap | Port Scanning |
| ssl | SSL Certificate Inspection |
| HTML & CSS | HTML Report Generation |
| Git | Version Control |
| GitHub | Repository Hosting |
| Kali Linux | Development Environment |

---

## 🏗️ Architecture

```text
                    User Input
                         │
                         ▼
                 Target Parser
                         │
                         ▼
                  DNS Resolution
                         │
                         ▼
                 Reverse DNS Lookup
                         │
                         ▼
                   WHOIS Lookup
                         │
                         ▼
                  Nmap Port Scan
                         │
                         ▼
                 Banner Grabbing
                         │
                         ▼
               SSL Certificate Scan
                         │
                         ▼
             Subdomain Enumeration
                         │
                         ▼
              Deep Subdomain Scan
                         │
                         ▼
      TXT Report + HTML Report Generation
```
---

## 🚀 Usage

Interactive Mode

```bash
python3 main.py
```

Command Line Mode

```bash
python3 main.py google.com
```
---

## 📂 Project Structure

```text
EDITH-Recon
│
├── core/
├── data/
├── docs/
├── modules/
├── reports/
├── screenshots/
│
├── banner.py
├── config.py
├── main.py
├── README.md
├── requirements.txt
└── LICENSE
```
---

## 📑 Generated Reports

EDITH Recon automatically generates:

- 📄 Professional TXT Report
- 🌐 Professional HTML Report

Each report contains:

- Target Information
- WHOIS Details
- Open Ports
- Banner Information
- SSL Information
- Enumerated Subdomains
- Scan Summary
  
  ---

## 🚀 Roadmap

### ✅ v1.1.0

- DNS Lookup
- Reverse DNS
- WHOIS
- Nmap Integration
- Banner Grabbing
- SSL Inspection
- Subdomain Enumeration
- Deep Scan
- TXT Reports
- HTML Reports

### 🔜 v1.2

- JSON Export
- PDF Report
- DNS Record Enumeration
- HTTP Security Headers
- Technology Detection
- Multi-threaded Enumeration

---

## ⚠️ Disclaimer

This project is intended for educational purposes and authorized security assessments only.

Always obtain permission before scanning any target.

---

## 📄 License

MIT License

---

## 👨‍💻 Author

**Mohammad Aliraza**

Computer Engineering Graduate

Cybersecurity Enthusiast

---

# 🛡️ EDITH Recon v1.1.0

> **Stay Curious. Stay Ethical.**

