import asyncio
from websockets.asyncio.client import connect
from websockets import exceptions
import json


BASE_URL = "wss://fstream.binance.com"
ENDPOINT = "ws/bnbusdt@aggTrade"


async def hello():
    url = f"{BASE_URL}/{ENDPOINT}"
    async with connect(url) as websocket:
        print("Connected to Binance WebSocket!")

        try:
            while True:
                message = await websocket.recv()  # Receive messages from the WebSocket
                data = json.loads(message)
                # Extract relevant data from the message
                price = data["p"]  # 'p' is the price field for aggTrade
                quantity = data["q"]  # 'q' is the quantity field for aggTrade
                print(f"Price: {price}, Quantity: {quantity}")

        except exceptions.ConnectionClosed as e:
            print(f"Connection closed: {e}")


if __name__ == "__main__":
    asyncio.run(hello())
