import ssl
import socket


def run(target):

    print("========== SSL ==========\n")

    try:

        context = ssl.create_default_context()

        with socket.create_connection((target.original, 443), timeout=5) as sock:

            with context.wrap_socket(sock, server_hostname=target.original) as secure_sock:

                certificate = secure_sock.getpeercert()

                subject = dict(x[0] for x in certificate["subject"])
                issuer = dict(x[0] for x in certificate["issuer"])

                target.ssl_subject = subject.get("commonName")
                target.ssl_issuer = issuer.get("commonName")
                target.ssl_expiry = certificate.get("notAfter")

                print(f"[+] Common Name : {target.ssl_subject}")
                print(f"[+] Issuer      : {target.ssl_issuer}")
                print(f"[+] Expires On  : {target.ssl_expiry}")
                print("[+] SSL Handshake Successful\n")

    except Exception as e:

        target.ssl_subject = None
        target.ssl_issuer = None
        target.ssl_expiry = None

        print(f"[-] SSL Scan Failed: {e}\n")