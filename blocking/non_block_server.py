from socket import socket, AF_INET, SOCK_STREAM, error as socket_error, timeout as sock_timeout

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(("127.0.0.1", 8888))
sock.listen(5)

# sock.setblocking(True)
sock.settimeout(5)
# sock.settimeout(0) => sock.setblocking(False)
# sock.settimeout(None) => sock.setblocking(True)

try:
    client, addr = sock.accept()
except socket_error:
    print("No connections")
# except sock_timeout:
#     print("Time Out")
else:
    result = client.recv(1024)
    client.close()
    print("Message: ", result.decode("utf-8"))
