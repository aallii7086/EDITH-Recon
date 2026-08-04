import nmap


def print_scan(scanner, target):

    target.open_ports = []

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

                    target.open_ports.append({
                        "port": port,
                        "protocol": protocol,
                        "service": port_info["name"]
                    })

        print()


def run(target, profile=None):

    print("========== NMAP SCAN ==========\n")

    scanner = nmap.PortScanner()

    if profile is None:

        print("Select Port Scan Profile\n")

        print("1. Top 100")
        print("2. Top 1000")
        print("3. Custom\n")

        choice = input("Choice : ").strip()

        if choice == "1":

            profile = "--top-ports 100"

        elif choice == "2":

            profile = "--top-ports 1000"

        elif choice == "3":

            ports = input("Enter Ports (Example: 80,443 or 1-1000): ")

            scanner.scan(target.original, ports=ports)

            print_scan(scanner, target)

            return "custom"

        else:

            print("[-] Invalid Choice\n")

            return None

    scanner.scan(target.original, arguments=profile)

    print_scan(scanner, target)

    return profile