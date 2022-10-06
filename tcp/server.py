from socket import socket, AF_INET, SOCK_STREAM

_socket = socket(AF_INET, SOCK_STREAM)
_socket.bind(("127.0.0.1", 8888))
_socket.listen(5)

while True:
    try:
        client, addres = _socket.accept()
    except KeyboardInterrupt as ex:
        _socket.close()
        break
    else:
        result = client.recv(1024)
        client.close()
        print("TSP Message:", result.decode("utf-8"))
        