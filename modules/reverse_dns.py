import socket


def run(target):

    print("========== REVERSE DNS ==========")

    try:

        hostname = socket.gethostbyaddr(target.ip)[0]

        target.hostname = hostname

        print(f"Hostname : {hostname}\n")

    except socket.herror:

        print("[-] Reverse DNS record not found.\n")