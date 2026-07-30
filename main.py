import whois
import socket
import sys

from colorama import Fore, Style
from banner import show_banner , show_footer

services = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}


def format_date(date_value):
    if isinstance(date_value, list):
        date_value = date_value[0]

    if date_value:
        return str(date_value).split()[0]

    return "Not Available"


def main():
    show_banner()

    if len(sys.argv) >= 2:
        target = sys.argv[1].strip()

    else: 
        target = input("Enter Target: ").strip()

    if not target:
        print("[-] Error: Target cannot be empty.")
        return

    print(f"[+] Target Accepted: {target}")

    report_path = f"reports/{target}_report.txt"

    with open(report_path, "w") as report:

        report.write("EDITH RECON REPORT\n")
        report.write("=" * 40 + "\n\n")
        report.write(f"Target: {target}\n\n")

        try:
            ip = socket.gethostbyname(target)

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

            # WHOIS
            try:
                domain_info = whois.whois(target)

                print("========== WHOIS ==========")
                print(f"Registrar: {domain_info.get('registrar')}")
                print(f"Creation Date: {format_date(domain_info.get('creation_date'))}")
                print(f"Expiration Date: {format_date(domain_info.get('expiration_date'))}")

                report.write("========== WHOIS ==========\n")
                report.write(f"Registrar: {domain_info.get('registrar')}\n")
                report.write(f"Creation Date: {format_date(domain_info.get('creation_date'))}\n")
                report.write(f"Expiration Date: {format_date(domain_info.get('expiration_date'))}\n\n")

            except Exception:
                print("[-] WHOIS lookup failed.\n")
                report.write("WHOIS lookup failed.\n\n")

            # Port Scan
            for port in range(22, 81):

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3)

                result = s.connect_ex((ip, port))

                if result == 0:

                    service = services.get(port, "Unknown")

                    print(f"[+] Port {port}/tcp OPEN ({service})")
                    report.write(f"[+] Port {port}/tcp OPEN ({service})\n")

                    # Banner Grabbing
                    if port == 80:

                        try:

                            request = (
                                f"GET / HTTP/1.1\r\n"
                                f"Host: {target}\r\n"
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

            print(f"\n[+] Report saved to: {report_path}")
            print(Fore.CYAN + "═" * 60)

            show_footer()

        except socket.gaierror:
            print("[-] Unable to resolve domain.")
            report.write("Unable to resolve domain.\n")


if __name__ == "__main__":
    main()
