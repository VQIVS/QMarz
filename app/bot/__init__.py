from flask import Blueprint

bp = Blueprint('bot', __name__)

from app.bot import bot
