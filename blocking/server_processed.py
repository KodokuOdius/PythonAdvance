from socket import socket, AF_INET, SOCK_STREAM, error as socket_error

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(("127.0.0.1", 8888))
sock.listen(5)
sock.setblocking(False)

while True:
    try:
        client, addr = sock.accept()
    except socket_error:
        print("No Clients")
        # sleep(100)
    except KeyboardInterrupt:
        break
    else:
        client.setblocking(True)
        result = client.recv(1024)
        client.close()
        print("Message: ", result.decode("utf-8"))
        break
