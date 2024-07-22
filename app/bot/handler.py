from telebot import TeleBot
from app.bot.operation import ManiHandler

def setup_handlers(bot: TeleBot):
    handler = ManiHandler(bot)

    @bot.message_handler(commands=['start'])
    def handle_start(message):
        handler.start(message)
    @bot.message_handler(func=lambda message: message.text == "💡 راهنما‌ی سرویس")
    def tutorial(message):
        handler.tutorial(message)
    @bot.message_handler(func=lambda message: message.text == "💬 پشتیبانی")
    def support(message):
        handler.support(message)
    @bot.message_handler(func= lambda message: message.text == "🧪دریافت سرور تست")
    def test(message):
        handler.test_sub(message)

