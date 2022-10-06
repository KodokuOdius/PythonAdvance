from socketserver import BaseRequestHandler, UDPServer


class EchoUDPHandler(BaseRequestHandler):
    def handle(self) -> None:
        data, socket = self.request
        print(f"Address: {self.client_address[0]}")
        print(f"Data: {data.decode()}")
        socket.sendto(data, self.client_address)


if __name__ == "__main__":
    with UDPServer(("127.0.0.1", 8888), EchoUDPHandler) as server:
        server.serve_forever()
