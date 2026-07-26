import socket


def main():
    print("=" * 50)
    print("      NETWORK RECON TOOLKIT v1.3")
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

        except socket.gaierror:
            print("[-] Unable to resolve domain.")


if __name__ == "__main__":
    main()
