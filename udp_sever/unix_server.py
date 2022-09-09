import os
import socket

unix_socket_name = "unix.sock"
_socket = socket.socket(socket.AF_UNIX, socket,socket.SOCK_DGRAM)

if os.path.exists(unix_socket_name):
    os.remove(unix_socket_name)

_socket.bind(unix_socket_name)

while True:
    try:
        result = _socket.recv(1024)
    except KeyboardInterrupt as ex:
        _socket.close()
    else:
        print("Unix Message:", result.decode("utf-8"))
        