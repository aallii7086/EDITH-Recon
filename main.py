import whois
import socket
import sys

from core.parser import TargetParser
from colorama import Fore, Style
from banner import show_banner , show_footer
from modules import whois_lookup

services = {
    20: "FTP-Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP",
    68: "DHCP",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    111: "RPC",
    123: "NTP",
    135: "MS RPC",
    137: "NetBIOS",
    138: "NetBIOS Datagram",
    139: "NetBIOS Session",
    143: "IMAP",
    161: "SNMP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    465: "SMTPS",
    587: "SMTP Submission",
    993: "IMAPS",
    995: "POP3S",
    1433: "MSSQL",
    1521: "Oracle",
    2049: "NFS",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP-Alt",
    8443: "HTTPS-Alt"
}


def format_date(date_value):
    if isinstance(date_value, list):
        date_value = date_value[0]

    if date_value:
        return str(date_value).split()[0]

    return "Not Available"


def main():
    show_banner()

    parser = TargetParser()

    if len(sys.argv) >= 2:
        target = parser.parse(sys.argv[1])
    else: 
        target = parser.parse(input("Enter Target:"))

    if not target:
        print("[-] Error: Target cannot be empty.")
        return

    print(f"[+] Target Accepted: {target.original}")

    report_path = f"reports/{target.original}_report.txt"

    with open(report_path, "w") as report:

        report.write("EDITH RECON REPORT\n")
        report.write("=" * 40 + "\n\n")
        report.write(f"Target: {target}\n\n")

        try:
            ip = socket.gethostbyname(target.original)

            print(f"[+] IP Address: {ip}\n")
            report.write(f"IP Address: {ip}\n\n")

            # Reverse DNS
            try:
                hostname = socket.gethostbyaddr(ip)[0]

                print(f"[+] Hostname: {hostname}\n")
                report.write(f"Hostname: {hostname}\n\n")

            except socket.herror:
                print("[-] Reverse DNS record not found.\n")
                report.write("Hostname: Reverse DNS record not found\n\n")

            # WHOIS LOOKUP

            whois_lookup.run(target)
            # Port Scan

            print("\n========== PORT SCAN ==========")
            print("[*] Scanning common ports...\n")

            common_ports = [
            20,21,22,23,25,
            53,67,68,69,
            80,110,111,123,
            135,137,138,139,
            143,161,389,
            443,445,465,
            587,993,995,
            1433,1521,
            2049,3306,
            3389,5432,
            5900,6379,
            8080,8443
            ]
            found = False

            for port in common_ports:

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)

                result = s.connect_ex((ip, port))

                if result == 0:

                    found = True

                    service = services.get(port, "Unknown")

                    print(f"[+] Port {port}/tcp OPEN ({service})")
                    report.write(f"[+] Port {port}/tcp OPEN ({service})\n")



                    # Banner Grabbing
                    if port == 80:

                        try:

                            request = (
                                f"GET / HTTP/1.1\r\n"
                                f"Host: {target.original}\r\n"
                                f"Connection: close\r\n\r\n"
                            )

                            s.send(request.encode())

                            banner = s.recv(1024).decode(errors="ignore")

                            print("\n------ Banner ------")
                            print(banner.split("\r\n")[0])

                            report.write("\n------ Banner ------\n")
                            report.write(banner.split("\r\n")[0] + "\n")

                            for line in banner.split("\r\n"):
                                if line.lower().startswith("server:"):
                                    print(line)
                                    report.write(line + "\n")

                            print("--------------------\n")
                            report.write("--------------------\n\n")

                        except Exception as e:
                            print(f"[-] Banner grab failed: {e}")
                            report.write(f"Banner grab failed: {e}\n")

                s.close()

            if not found:
                print("[-] No common ports are open.")
                report.write("No common ports are open.\n")

            print("[+] Port scan completed.\n")

            print(f"\n[+] Report saved to: {report_path}")
            print(Fore.CYAN + "═" * 60)

            show_footer()

        except socket.gaierror:
            print("[-] Unable to resolve domain.")
            report.write("Unable to resolve domain.\n")


if __name__ == "__main__":
    main()
