import asyncio
import json

from websockets import exceptions
from websockets.asyncio.client import connect

BASE_URL = "wss://fstream.binance.com"
ENDPOINT = "ws/bnbusdt@aggTrade"


async def listen() -> None:
    url = f"{BASE_URL}/{ENDPOINT}"
    async with connect(url) as websocket:
        print("Connected to Binance WebSocket!")

        try:
            while True:
                message = await websocket.recv()
                data = json.loads(message)
                price = data["p"]
                quantity = data["q"]
                print(f"Price: {price}, Quantity: {quantity}")

        except exceptions.ConnectionClosed as e:
            print(f"Connection closed: {e}")


if __name__ == "__main__":
    asyncio.run(listen())
