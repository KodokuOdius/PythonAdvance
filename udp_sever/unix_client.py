import socket

_socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
_socket.sendto(b"Test Unix Message", "unix.sock")