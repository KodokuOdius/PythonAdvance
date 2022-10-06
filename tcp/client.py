from socket import socket, AF_INET, SOCK_STREAM

_socket = socket(AF_INET, SOCK_STREAM)
_socket.connect(("127.0.0.1", 8888))
_socket.send(b"TSP Test Message")
_socket.close()
