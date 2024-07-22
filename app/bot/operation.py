from telebot.types import Message
from telebot import TeleBot
from app import create_app
from app.repositories.user_repository import UserRepository
from app.repositories.subscription_repository import SubscriptionRepository

from .keybaord import Keyboard
from dotenv import load_dotenv
import os
from .utils import APIManager
import uuid 


# TODO: Do not pass the bot in tests
# bot = TeleBot("Bot_Token")

# Initialize Flask app
app = create_app()
keybaord = Keyboard()
API_URL = os.getenv("API_URL")
apiManager = APIManager(API_URL)
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
token = apiManager.get_token(USERNAME, PASSWORD)

class ManiHandler:
    def __init__(self, bot):
        self.bot = bot

    def start(self, message: Message):
        user_id = str(message.chat.id)
        try:
            with app.app_context():
                userRepo = UserRepository()
                user = userRepo.create(user_id)
                self.bot.send_message(user_id, "Welcome!", reply_markup=keybaord.mainKeyboard)
        except ValueError as e:
            if "User with this username already exists" in str(e):
                self.bot.send_message(user_id, f"Welcome back user: {user_id}", reply_markup=keybaord.mainKeyboard)
            else:
                self.bot.send_message(user_id, f"Error: {str(e)}")
        except Exception as e:
            self.bot.send_message(user_id, f"An unexpected error occurred: {str(e)}")

    def tutorial(self, message: Message):
        user_id = str(message.chat.id)
        msg = "Please choose your OS first"
        self.bot.send_message(user_id, msg, reply_markup=keybaord.tutorialKeyboard)

    def support(self, message: Message):
        user_id = str(message.chat.id)
        load_dotenv()
        SUPPORT_ID = os.getenv("SUPPORT_ID") 
        msg = f"For support DM: {SUPPORT_ID}"
        print(SUPPORT_ID)
        self.bot.send_message(user_id, msg)

    def test_sub(self, message: Message):
        user_id = str(message.chat.id)
        TEST_LIMIT = os.getenv("TEST_LIMIT") 
        TEST_EXPIRE_DAYS =os.getenv("TEST_EXPIRE_DAYS")
        res = apiManager.create_user(username=uuid.UUID, data_limit=TEST_LIMIT,expire=TEST_EXPIRE_DAYS, access_token=token)
        if res is not None:
            subscription_url = res.get("subscription_url")
            subscription_size = f"{TEST_LIMIT}"
            usage_method = "از دکمه راهنمای سرویس استفاده کنید"
            text = (
                    f"🎉 اشتراک تست شما:\n{subscription_url}\n\n"
                    f"🔋 حجم اشتراک شما: {subscription_size}\n\n"
                    f"🔍 نحوه استفاده: {usage_method}"
                )
            self.bot.send_message(user_id, text)
        else:
                self.bot.send_message(
                    user_id, "خطایی رخ داده است. لطفا دوباره تلاش کنید"
                )
                subRepo = SubscriptionRepository()
                sub = subRepo.create(plan="test", price=0, duration_days=1, user_id=user_id)
                print(sub)
        
        self.bot.send_message(user_id, text)
