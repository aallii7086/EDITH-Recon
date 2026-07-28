import socket

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

def main():
    print("=" * 50)
    print("      NETWORK RECON TOOLKIT v1.4")
    print("=" * 50)

    target = input("Enter Target: ")
    target = target.strip()

    if len(target) == 0:
        print("[-] Error: Target cannot be empty.")
    else:
        print("[+] Target Accepted:", target)

        try:
            ip = socket.gethostbyname(target)
            print("[+] IP Address:", ip)

            for port in range(22, 81):
                s = socket.socket()
                s.settimeout(3)

                result = s.connect_ex((ip, port))

                s.close()

               # print(f"Port {port} -> Result = {result}")

                if result == 0:
                    service = services.get(port,"UNKNOWN")
                    print(f"[+] Port {port}/tcp OPEN ({service})")

        except socket.gaierror:
            print("[-] Unable to resolve domain.")


if __name__ == "__main__":
    main()
