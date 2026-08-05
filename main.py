import sys

from banner import show_banner, show_footer

from core.parser import TargetParser

from modules import dns_lookup
from modules import reverse_dns
from modules import whois_lookup
from modules import nmap_scan
from modules import banner_grab
from modules import ssl_scan
from modules import reporter
from modules import subdomain
from modules import report


def main():

    show_banner()

    parser = TargetParser()

    if len(sys.argv) >= 2:
        target = parser.parse(sys.argv[1])

    else:
        target = parser.parse(input("Enter Target: ").strip())

    print(f"\n[+] Target Accepted : {target.original}\n")

    dns_lookup.run(target)

    if target.ip:


        reverse_dns.run(target)

    whois_lookup.run(target)

    selected_profile = nmap_scan.run(target)

    banner_grab.run(target)

    ssl_scan.run(target)

    subdomain.run(target, selected_profile)

    reporter.run(target)

    report.run(target)

    print("=" * 60)
    print("[+] Scan Completed Successfully")
    print("=" * 60)
    print()

    show_footer()


if __name__ == "__main__":
    main()