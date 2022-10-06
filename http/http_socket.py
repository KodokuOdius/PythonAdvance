from socket import socket, AF_INET, SOCK_STREAM

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(("example.com", 80))
content_items = [
    "GET / HTTP/1.1",
    "Host: example.com",
    "Connection: keep-alive",
    "Accept: text/html",
    "\n"
]
content = "\n".join(content_items)
print("==== HTTP MESSAGE ====")
print(content)
print("=== END OF MESSAGE ===")
sock.send(content.encode())
result = sock.recv(10024)
print(result.decode())
