import whois

from core.utils import format_date


def run(target):

    print("========== WHOIS ==========")

    try:

        domain_info = whois.whois(target.original)

        print(f"Registrar       : {domain_info.get('registrar')}")
        print(f"Creation Date   : {format_date(domain_info.get('creation_date'))}")
        print(f"Expiration Date : {format_date(domain_info.get('expiration_date'))}")

        print()

    except Exception:

        print("[-] WHOIS Lookup Failed\n")