
import nest_asyncio
nest_asyncio.apply()

from aiohttp import web
# from plugins import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode

import sys
from datetime import datetime

import sys
from datetime import datetime

from info import API_HASH, APP_ID, TG_BOT_TOKEN, PORT


# Bot = Client(
#     "my_account",
#     api_id = APP_ID,
#     api_hash = API_HASH,
#     plugins={
#                 "root": "plugins"
#             },
#     bot_token = TG_BOT_TOKEN
#     )

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            bot_token=TG_BOT_TOKEN
        )

    async def start(self):
        super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

       
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()


print("I AM ALIVE")
Bot().run()

# Bot = Client(
#     "my_account",
#     api_id = 10755921,
#     api_hash = "d5e49fd3637cba407f17807d31c77977",
#     plugins={
#                 "root": "plugins"
#             },
#     bot_token = "5906626853:AAFzimXzHM4oV1QCT2xvkadzjvjRti7NMBk"
#     )
