import sys
import os
from dotenv import load_dotenv
from telebot import TeleBot


# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

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
