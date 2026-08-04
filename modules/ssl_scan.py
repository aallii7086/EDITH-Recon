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

                print(f"[+] Common Name : {subject.get('commonName')}")
                print(f"[+] Issuer      : {issuer.get('commonName')}")
                print(f"[+] Expires On  : {certificate.get('notAfter')}")
                print("[+] SSL Handshake Successful\n")

    except Exception as e:

        print(f"[-] SSL Scan Failed: {e}\n")