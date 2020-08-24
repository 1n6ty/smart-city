import logging, asyncio, websockets
from websockets import WebSocketServerProtocol

logging.basicConfig(level = logging.INFO)

class Server:

    async def distribute(self, ws: WebSocketServerProtocol):
        async for message in ws:
            logging.info(f'message: {message}')
            await ws.send('world!')

    async def wsHandler(self, ws: WebSocketServerProtocol, uri: str):
        await self.distribute(ws)


server = Server()
start_serve = websockets.serve(server.wsHandler, 'localhost', 4321)
loop = asyncio.get_event_loop()
loop.run_until_complete(start_serve)
loop.run_forever()