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

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Service is running', 200

@app.route('/health')
def health_check():
    # You can add more comprehensive health checks here
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(port=8000)  # Listen on all interfaces on port 80


if __name__ == '__main__':
    if not os.path.isdir(client.config.DOWNLOAD_LOCATION):
        os.makedirs(client.config.DOWNLOAD_LOCATION)
    client.run(main())
