"""
EDITH RECON
Target
Version: 1.2.0
"""


class Target:

    def __init__(self):

        # ==========================
        # Original Input
        # ==========================

        self.original = None

        self.target_type = None

        self.scheme = None

        self.hostname = None

        self.domain = None

        self.ip = None

        self.path = None

        self.query = None

        # ==========================
        # DNS
        # ==========================

        self.reverse_dns = None

        # ==========================
        # WHOIS
        # ==========================

        self.registrar = None

        self.creation_date = None

        self.expiration_date = None

        # ==========================
        # NMAP
        # ==========================

        self.open_ports = []

        # ==========================
        # Banner
        # ==========================

        self.banner = None

        self.server = None

        # ==========================
        # SSL
        # ==========================

        self.ssl_subject = None

        self.ssl_issuer = None

        self.ssl_expiry = None

        # ==========================
        # Subdomains
        # ==========================

        self.subdomains = []