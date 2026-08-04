import socket


def run(target):

    print("========== DNS ==========")

    try:

        ip = socket.gethostbyname(target.original)

        target.ip = ip

        print(f"IP Address : {ip}\n")

    except socket.gaierror:

        target.ip = None

        print("[-] DNS Lookup Failed\n")