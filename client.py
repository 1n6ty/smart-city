import asyncio
import websockets
import logging

logging.basicConfig(level = logging.INFO)

async def consumer(ws):
    async for message in ws:
        logging.info(f'Message: {message}')

async def consume(host, port):
    async with websockets.connect(f'ws://{host}:{port}') as ws:
        await ws.send('hello')
        await consumer(ws)
        await ws.recv()


loop = asyncio.get_event_loop()
loop.run_until_complete(consume("localhost", 4321))