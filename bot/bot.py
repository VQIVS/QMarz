import os
from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv()

# Get environment variables
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')

# Initialize Telegram client
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(bot_token=bot_token)
    print("Bot is running...")

with client:
    client.loop.run_until_complete(main())
