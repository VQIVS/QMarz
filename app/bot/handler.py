from telebot import TeleBot
from app.bot.operation import ManiHandler

def setup_handlers(bot: TeleBot):
    handler = ManiHandler(bot)

    @bot.message_handler(commands=['start'])
    def handle_start(message):
        handler.start(message)
