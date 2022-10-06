from socket import socket, AF_INET, SOCK_DGRAM, timeout as sock_timeout

# sock = socket(AF_INET, SOCK_STREAM)
# sock.bind(("127.0.0.1", 8888))

with socket(AF_INET, SOCK_DGRAM) as sock:
    # print("8888 is bind")
    sock.bind(("127.0.0.1", 8888))
    sock.settimeout(5)

    while True:
        try:
            result = sock.recv(1024)
            print("Message: ", result.decode("utf-8"))
        except sock_timeout:
            print("Time Out")
            break
