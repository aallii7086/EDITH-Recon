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

        print(first_line)

        for line in response.split("\r\n"):

            if line.lower().startswith("server:"):

                print(line)

        print("--------------------\n")

        sock.close()

    except Exception as e:

        print(f"[-] Banner grab failed: {e}\n")