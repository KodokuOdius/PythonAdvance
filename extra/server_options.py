from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_BROADCAST, SO_REUSEADDR

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(("127.0.0.1", 8888))
sock.listen(5)
# Широковещательная Datagram
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

# Переиспользование адресса / порта
# sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

client, addr = sock.accept()
result = client.recv(1024)
client.close()

print("Message: ", result.decode("utf-8"))
