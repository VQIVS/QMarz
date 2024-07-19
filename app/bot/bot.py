import os
from dotenv import load_dotenv
from telebot import TeleBot
from app.bot.handler import setup_handlers

# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = TeleBot(BOT_TOKEN)

# Set up handlers
setup_handlers(bot)


def main():
    bot.infinity_polling()


if __name__ == "__main__":
    main()
