from telebot import types


class KeyboardCreator:
    def __init__(self):
        pass

    @staticmethod
    def create(buttons):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for button_row in buttons:
            keyboard.add(*button_row)
        return keyboard


class Keyboard:
    def __init__(self):
        pass

    mainButtons = [
        [types.KeyboardButton("⭐️ خرید سرویس")],
        [
            types.KeyboardButton("👤 اشتراک‌های من"),
            types.KeyboardButton("🧪دریافت سرور تست"),
        ],
        [types.KeyboardButton("💡 راهنما‌ی سرویس"), types.KeyboardButton("💬 پشتیبانی")],
        [
            types.KeyboardButton("🛍 خرید عمده️"),
            types.KeyboardButton("👨‍👩‍👧‍👧 معرفی به دوستان"),
        ],
    ]
    mainKeyaboard = KeyboardCreator.create(mainButtons)
