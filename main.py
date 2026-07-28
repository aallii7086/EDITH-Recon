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
    print("      NETWORK RECON TOOLKIT v1.5")
    print("=" * 50)

    target = input("Enter Target: ").strip()

    if not target:
        print("[-] Error: Target cannot be empty.")
        return

    print(f"[+] Target Accepted: {target}")

    try:
        ip = socket.gethostbyname(target)
        print(f"[+] IP Address: {ip}\n")

        for port in range(22, 81):

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)

            result = s.connect_ex((ip, port))

            if result == 0:
                service = services.get(port, "Unknown")
                print(f"[+] Port {port}/tcp OPEN ({service})")

                # Banner Grabbing (HTTP only)
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

                        for line in banner.split("\r\n"):
                            if line.lower().startswith("server:"):
                                print(line)

                        print("--------------------\n")

                    except Exception as e:
                        print(f"[-] Banner grab failed: {e}")

            s.close()

    except socket.gaierror:
        print("[-] Unable to resolve domain.")


if __name__ == "__main__":
    main()
