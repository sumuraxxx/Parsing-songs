from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(token=os.environ.get('TOKEN_TG'), parse_mode=ParseMode.HTML)
dp = Dispatcher()
