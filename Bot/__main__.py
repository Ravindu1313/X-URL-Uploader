import os
import logging
from . import client
from aiohttp import ClientSession
from pyrogram import idle


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)


async def main():
    await client.startup()
    await client.bot.set_bot_commands(client.config.BOT_COMMANDS)
    session = ClientSession()
    client.session = session
    if client.config.AUTH_USERS:
        client.config.AUTH_USERS.append(client.config.OWNER_ID)
    client.logger.info(f'{client.bot.me.first_name} Started!')
    await idle()

from flask import Flask
 
# instance of flask application
app = Flask(__name__)
 
# home route that returns below text 
# when root url is accessed
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
 
if __name__ == '__main__':
    app.run(debug=True, port=8000)


if __name__ == '__main__':
    if not os.path.isdir(client.config.DOWNLOAD_LOCATION):
        os.makedirs(client.config.DOWNLOAD_LOCATION)
    client.run(main())
