from core.utils import format_date
import whois


def run(target):

    try:

        domain_info = whois.whois(target.original)

        print("========== WHOIS ==========")
        print(f"Registrar: {domain_info.get('registrar')}")
        print(f"Creation Date: {format_date(domain_info.get('creation_date'))}")
        print(f"Expiration Date: {format_date(domain_info.get('expiration_date'))}")

    except Exception:
        print("[-] WHOIS lookup failed.")