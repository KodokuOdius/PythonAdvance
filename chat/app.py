import asyncio
import websockets
from websockets.legacy.client import WebSocketClientProtocol
from websockets.legacy.server import serve


clients = []


async def send_message(message: str):
    for client in clients:
        await client.send(message)


async def new_client_connected(client_socket: WebSocketClientProtocol, path: str):
    print("New Client Connected")
    clients.append(client_socket)

    while True:
        new_message = await client_socket.recv()
        print("Client send message: ", new_message, path)
        await send_message(new_message)


async def start_server():
    print("start server")
    await serve(new_client_connected, "127.0.0.1", 5050)



if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(start_server())
    event_loop.run_forever()
