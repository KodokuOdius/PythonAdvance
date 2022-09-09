from socket import socket, AF_INET, SOCK_DGRAM

_socket = socket(AF_INET, SOCK_DGRAM)
_socket.bind(("127.0.0.1", 8888))
print("Start Server")
result = _socket.recv(1024)
print("Message: ", result.decode("utf-8"))
_socket.close()