import whois

from core.utils import format_date


def run(target):

    print("========== WHOIS ==========")

    try:

        domain_info = whois.whois(target.original)

        target.registrar = domain_info.get("registrar")
        target.creation_date = format_date(domain_info.get("creation_date"))
        target.expiration_date = format_date(domain_info.get("expiration_date"))

        print(f"Registrar       : {target.registrar}")
        print(f"Creation Date   : {target.creation_date}")
        print(f"Expiration Date : {target.expiration_date}")

        print()

    except Exception:

        target.registrar = None
        target.creation_date = None
        target.expiration_date = None

        print("[-] WHOIS Lookup Failed\n")