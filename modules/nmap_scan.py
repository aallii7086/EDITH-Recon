import nmap

def print_scan(scanner):

    for host in scanner.all_hosts():

        print(f"\nHost : {host}")

        for protocol in scanner[host].all_protocols():

            print(f"\nProtocol : {protocol}")

            for port in sorted(scanner[host][protocol].keys()):

                port_info = scanner[host][protocol][port]

                if port_info["state"] == "open":

                    print(
                        f"[+] Port {port}/{protocol} OPEN ({port_info['name']})"
                    )

        print()


def run(target):

    print("========== NMAP SCAN ==========\n")

    print("Select Port Scan Profile\n")

    print("1. Top 100")
    print("2. Top 1000")
    print("3. Custom\n")

    choice = input("Choice : ").strip()

    scanner = nmap.PortScanner()

    if choice == "1":

        arguments = "--top-ports 100"

    elif choice == "2":

        arguments = "--top-ports 1000"

    elif choice == "3":

        ports = input("Enter Ports (Example: 80,443 or 1-1000): ")

        scanner.scan(target.original, ports=ports)

        print_scan(scanner)

        return

    else:

        print("[-] Invalid Choice\n")

        return

    scanner.scan(target.original, arguments=arguments)

    print_scan(scanner)