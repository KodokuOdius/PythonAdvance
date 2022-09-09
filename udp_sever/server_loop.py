from socket import socket, AF_INET, SOCK_DGRAM

_socket = socket(AF_INET, SOCK_DGRAM)
_socket.bind(("127.0.0.1", 8888))

while True:
    try:
        result = _socket.recv(1024)
    except KeyboardInterrupt as ex:
        _socket.close()
        break
    else:
        print("Message:", result.decode("utf-8"))
