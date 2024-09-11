from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import os
import dotenv
dotenv.load_dotenv()
storage = MemoryStorage()

bot = Bot(os.getenv('BOT_TOKEN'))

dp = Dispatcher(bot, storage= storage)