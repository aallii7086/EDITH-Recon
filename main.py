import socket

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
                s.settimeout(1)

                result = s.connect_ex((ip, port))

                s.close()

                print(f"POrt {port} -> Result = {result}")

                if result == 0:
                    print("[+] Port", port, "is OPEN")
                else:
                    print("[-] Port", port, "is CLOSED")

        except socket.gaierror:
            print("[-] Unable to resolve domain.")


if __name__ == "__main__":
    main()
