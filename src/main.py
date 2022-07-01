from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from dotenv import load_dotenv

from handlers.register_handlers import register_all_handlers


# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.MARKDOWN_V2)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

register_all_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
