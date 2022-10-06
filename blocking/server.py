from socket import socket, AF_INET, SOCK_STREAM

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(("127.0.0.1", 8888))
sock.listen(5)
sock.setblocking(False)

client, addr = sock.accept()
result = client.recv(1024)
client.close()

print("Message: ", result.decode("utf-8"))
