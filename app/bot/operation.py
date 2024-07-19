from telebot.types import Message
from app import create_app
from app.repositories.user_repository import UserRepository
from .keybaord import Keyboard

# Initialize Flask app
app = create_app()
userRepo = UserRepository()
kebaord = Keyboard()

class ManiHandler:
    def __init__(self, bot):
        self.bot = bot

    def start(self, message: Message):
        user_id = str(message.chat.id)
        try:
            with app.app_context():
                user = userRepo.create(user_id)
                self.bot.send_message(user_id, "Welcome!", reply_markup=kebaord.mainKeyaboard)
        except ValueError as e:
            if "User with this username already exists" in str(e):
                self.bot.send_message(user_id, f"Welcome back user: {user_id}", reply_markup=kebaord.mainKeyaboard)
            else:
                self.bot.send_message(user_id, f"Error: {str(e)}")
        except Exception as e:
            self.bot.send_message(user_id, f"An unexpected error occurred: {str(e)}")
                
    
