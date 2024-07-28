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
from app.utils.logger_config import get_logger

# Initialize environment variables
load_dotenv(override=True)
API_URL = os.getenv("API_URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
TEST_LIMIT = float(os.getenv("TEST_LIMIT", 0))
TEST_EXPIRE_DAYS = int(os.getenv("TEST_EXPIRE_DAYS", 0))
SUPPORT_ID = os.getenv("SUPPORT_ID")

# Initialize API Manager and get token
apiManager = APIManager(API_URL)
token = apiManager.get_token(USERNAME, PASSWORD)

# Initialize Flask app and keyboard
app = create_app()
keyboard = Keyboard()

# Get logger instance
logger = get_logger("app_logger")

class ManiHandler:
    def __init__(self, bot: TeleBot):
        self.bot = bot

    def start(self, message: Message):
        user_id = str(message.chat.id)
        try:
            with app.app_context():
                userRepo = UserRepository()
                user = userRepo.create(user_id)
                self.bot.send_message(user_id, "Welcome!", reply_markup=keyboard.mainKeyboard)
                logger.info(f"User {user_id} created and welcomed.")
        except ValueError as e:
            if "User with this username already exists" in str(e):
                self.bot.send_message(user_id, f"Welcome back user: {user_id}", reply_markup=keyboard.mainKeyboard)
                logger.info(f"Existing user {user_id} welcomed back.")
            else:
                self.bot.send_message(user_id, f"Error: {str(e)}")
                logger.error(f"Error creating user {user_id}: {str(e)}")
        except Exception as e:
            logger.error(f"Unexpected error occurred in start method for user {user_id}: {e}", exc_info=True)
            self.bot.send_message(user_id, f"An unexpected error occurred: {str(e)}")

    def tutorial(self, message: Message):
        user_id = str(message.chat.id)
        msg = "Please choose your OS first"
        self.bot.send_message(user_id, msg, reply_markup=keyboard.tutorialKeyboard)
        logger.info(f"User {user_id} prompted to choose OS.")

    def support(self, message: Message):
        user_id = str(message.chat.id)
        msg = f"For support DM: {SUPPORT_ID}"
        self.bot.send_message(user_id, msg)
        logger.info(f"Support information sent to user {user_id}.")

    def test_sub(self, message: Message):
        user_id = str(message.chat.id)
        logger.debug(f"Initiating test_sub for user {user_id} with limit {TEST_LIMIT} and expire days {TEST_EXPIRE_DAYS}")
        
        try:
            with app.app_context():
                subRepo = SubscriptionRepository()
                user_subscriptions = subRepo.get_by_user_id(user_id)
                
                # Check if any of the user's subscriptions have a "test" plan
                if any(sub.plan == "test" for sub in user_subscriptions):
                    self.bot.send_message(user_id, "You have already gotten a test plan subscription before.")
                    logger.info(f"User {user_id} already has a test plan subscription.")
                    return

                res = apiManager.create_user(username=user_id, data_limit=TEST_LIMIT, expire=TEST_EXPIRE_DAYS, access_token=token)
                if res is not None:
                    subscription_url = res.get("subscription_url")
                    proxies = res.get("proxies")
                    subscription_size = f"{TEST_LIMIT}"
                    usage_method = "از دکمه راهنمای سرویس استفاده کنید"
                    text = (
                        f"🎉 اشتراک تست شما:\n{subscription_url}\n\n"
                        f"🔋 حجم اشتراک شما: {subscription_size}\n\n"
                        f"🔍 نحوه استفاده: {usage_method}"
                        f"لینک ها : {proxies}"
                    )
                    self.bot.send_message(user_id, text)
                    logger.info(f"Test subscription created for user {user_id}.")
                else:
                    self.bot.send_message(user_id, "خطایی رخ داده است. لطفا دوباره تلاش کنید")
                    sub = subRepo.create(plan="test", price=0, duration_days=1, user_id=user_id)
                    self.bot.send_message(user_id, "خطایی رخ داده است. لطفا دوباره تلاش کنید")
                    logger.warning(f"Subscription creation failed for user {user_id}, fallback created.")
        except Exception as e:
            logger.error(f"Unexpected error occurred in test_sub method for user {user_id}: {e}", exc_info=True)
            self.bot.send_message(user_id, "An unexpected error occurred. Please try again later.")
