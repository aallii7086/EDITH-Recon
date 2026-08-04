import socket


def run(target):

    print("========== REVERSE DNS ==========")

    try:

        hostname = socket.gethostbyaddr(target.ip)[0]

        target.reverse_dns = hostname
        target.hostname = hostname

        print(f"Hostname : {hostname}\n")

    except socket.herror:

        target.reverse_dns = None

        print("[-] Reverse DNS record not found.\n")