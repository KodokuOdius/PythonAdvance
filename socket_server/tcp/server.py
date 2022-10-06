from socketserver import BaseRequestHandler, TCPServer


class EchoUDPHandler(BaseRequestHandler):
    def handle(self) -> None:
        data = self.request.recv(1024).strip()
        print(f"Address: {self.client_address[0]}")
        print(f"Data: {data.decode()}")
        self.request.sendall(data)


if __name__ == "__main__":
    with TCPServer(("127.0.0.1", 8888), EchoUDPHandler) as server:
        server.serve_forever()
