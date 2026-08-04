import socket


def run(target):

    print("========== BANNER ==========\n")

    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)

        sock.connect((target.original, 80))

        request = (
            f"GET / HTTP/1.1\r\n"
            f"Host: {target.original}\r\n"
            f"Connection: close\r\n\r\n"
        )

        sock.send(request.encode())

        response = sock.recv(1024).decode(errors="ignore")

        print("------ Banner ------")

        first_line = response.split("\r\n")[0]

        target.banner = first_line

        print(first_line)

        target.server = None

        for line in response.split("\r\n"):

            if line.lower().startswith("server:"):

                target.server = line.replace("Server:", "").strip()

                print(line)

        print("--------------------\n")

        sock.close()

    except Exception as e:

        target.banner = None
        target.server = None

        print(f"[-] Banner grab failed: {e}\n")