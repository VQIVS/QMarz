from telebot import TeleBot
from app.bot.operation import ManiHandler
from app.bot.keybaord import Keyboard
from telebot.types import CallbackQuery


def setup_handlers(bot: TeleBot):
    handler = ManiHandler(bot)

    @bot.message_handler(func=lambda message: message.text == "⭐️ خرید سرویس")
    def buy_service(message):
        handler.show_service_options(message)

    @bot.callback_query_handler(func=lambda call: call.data in ["service_1T", "service_2T", "service_3T"])
    def service_selection(call: CallbackQuery):
        handler.handle_service_selection(call)

    @bot.message_handler(commands=["start"])
    def handle_start(message):
        handler.start(message)

    @bot.message_handler(func=lambda message: message.text == "💡 راهنما‌ی سرویس")
    def tutorial(message):
        handler.tutorial(message)

    @bot.message_handler(func=lambda message: message.text == "💬 پشتیبانی")
    def support(message):
        handler.support(message)

    @bot.message_handler(func=lambda message: message.text == "🧪دریافت سرور تست")
    def test(message):
        handler.test_sub(message)

    @bot.message_handler(func=lambda message: message.text == "👨‍👩‍👧‍👧 معرفی به دوستان")
    def refer(message):
        handler.send_referral_link(message)

    @bot.message_handler(func=lambda message: message.text == "🏆 امتیازات")
    def points_menu(message):
        handler.bot.send_message(message.chat.id, "Choose an option:", reply_markup=Keyboard.pointsKeyboard)

    @bot.message_handler(func=lambda message: message.text == "👀 مشاهده امتیازات")
    def show_points(message):
        handler.show_points(message)

    @bot.message_handler(func=lambda message: message.text == "🔙 بازگشت به منو اصلی")
    def go_back_to_main(message):
        handler.bot.send_message(message.chat.id, "Returning to the main menu.", reply_markup=Keyboard.mainKeyboard)

    @bot.callback_query_handler(func=lambda query: query.data == "joined")
    def handle_join(query):
        handler.handle_join(query)
