from socket import socket, AF_INET, SOCK_DGRAM
import sys

_socket = socket(AF_INET, SOCK_DGRAM)
if len(sys.argv) > 1:
    msg = sys.argv[1].encode("utf-8")
else:
    msg = b"Test Message"

_socket.sendto(msg, ("127.0.0.1", 8888))