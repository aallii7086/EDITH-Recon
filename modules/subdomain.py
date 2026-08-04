import socket

from core.target import Target

from modules import dns_lookup
from modules import nmap_scan
from modules import banner_grab
from modules import ssl_scan


def deep_scan(host, selected_profile):

    print("=" * 60)
    print(f"Target : {host['hostname']}")
    print("=" * 60)

    sub_target = Target()
    sub_target.original = host["hostname"]
    sub_target.ip = host["ip"]

    dns_lookup.run(sub_target)
    nmap_scan.run(sub_target, selected_profile)
    banner_grab.run(sub_target)
    ssl_scan.run(sub_target)

    print("\n[+] Deep Scan Complete\n")


def run(target, selected_profile):

    print("========== SUBDOMAIN ENUMERATION ==========\n")

    try:

        with open("data/subdomains.txt", "r") as file:
            words = file.read().splitlines()

        print(f"[+] Loaded {len(words)} subdomains.\n")

        found = []

        for word in words:

            subdomain = f"{word}.{target.original}"

            try:

                ip = socket.gethostbyname(subdomain)

                print(f"[{len(found)+1}] {subdomain}")
                print(f"    IP : {ip}\n")

                found.append({
                    "hostname": subdomain,
                    "ip": ip
                })

            except socket.gaierror:
                pass

        print("----------------------------------------")
        print(f"Total Subdomains Found : {len(found)}")
        print("----------------------------------------")

        if not found:

            print("[-] No subdomains found.\n")
            return

        print("\nChoose an Option\n")

        print("1. Scan All Subdomains")
        print("2. Scan Specific Subdomain")
        print("3. Continue to Report\n")

        choice = input("Choice : ").strip()

        # ======================================================
        # OPTION 1
        # ======================================================

        if choice == "1":

            print("\nWARNING!\n")
            print(f"You are about to deep scan {len(found)} subdomains.")
            print("This may take several minutes.\n")

            confirm = input("Continue? (Y/N): ").strip().upper()

            if confirm != "Y":

                print("\n[-] Scan Cancelled.\n")
                return

            print("\n========== DEEP SCAN ==========\n")

            for index, host in enumerate(found, start=1):

                print(f"\nScanning [{index}/{len(found)}]\n")

                deep_scan(host, selected_profile)

        # ======================================================
        # OPTION 2
        # ======================================================

        elif choice == "2":

            try:

                number = int(input("\nEnter Subdomain Number : "))

                if number < 1 or number > len(found):

                    print("\n[-] Invalid Number.\n")
                    return

                print("\n========== DEEP SCAN ==========\n")

                deep_scan(found[number - 1], selected_profile)

            except ValueError:

                print("\n[-] Please enter a valid number.\n")

        # ======================================================
        # OPTION 3
        # ======================================================

        elif choice == "3":

            print("\n[+] Continuing to Report...\n")

        else:

            print("\n[-] Invalid Choice.\n")

    except FileNotFoundError:

        print("[-] Wordlist not found.\n")