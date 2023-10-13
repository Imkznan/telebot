from telethon import TelegramClient,events
import logging
import socks

api_id=21390381
hash_id='a2fa709dd3771196455e5d360a944852'
token_bot='6026031880:AAGAJriUuOT9hq9cFZHk1bqkW31Ch6KmS14'
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

client = TelegramClient('anon', api_id, hash_id)

async def handler():
    # Good
    await client.send_message('@Im_kz_NAN','dadaxad')
    
client.start(bot_token=token_bot)
with client:
    client.loop.run_until_complete(handler())
