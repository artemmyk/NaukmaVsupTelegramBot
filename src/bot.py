import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

import src.routing.degree as degree
import src.routing.main_menu as main_menu

# import src.data.keyboards as keyboards

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    bot = Bot(token='5466806676:AAF0OooSN6amWLwqHgKd5nE7V7H3VxafERU')

    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(main_menu.router)
    dp.include_router(degree.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
