from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import filters
from aiogram.utils import exceptions
import asyncio


from db.operations import check_if_user_in_db, add_user_to_db, check_if_user_is_admin, get_all_chat_ids

from handlers.register_handlers import register_all_handlers
from keyboards.main_menu_keyboard import main_menu_keyboard

BOT_TOKEN = "5077592058:AAGPmoUShW56UGfVxNGrJ8c0BNHRPqM98-w"

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.MARKDOWN_V2)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

register_all_handlers(dp)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """

    # # check if user is in database (if not then add to db)
    # if not check_if_user_in_db(message.from_user.id):
    #     add_user_to_db(message.from_user.id)

    await message.answer("Привіт фреш.", reply_markup=main_menu_keyboard)


@dp.message_handler(filters.Text(contains="Повідомлення для всіх"))
async def admin(message: types.Message):
    """
    This handler will be called when user sends `/admin` command
    It will check if user is admin (in database) and call
    'Message for all' function
    """

    # TODO: create handler for message that will be sent to all users
    if check_if_user_is_admin(message.from_user.id):
        text = message.text.replace("Повідомлення для всіх", "")
        try:
            for user_id in get_all_chat_ids():
                await bot.send_message(user_id, text)
                await asyncio.sleep(.05)
        except:
            await message.reply("Error occurred")


async def send_message(user_id: int, text: str, disable_notification: bool = False) -> bool:
    """
    Safe messages sender
    :param user_id:
    :param text:
    :param disable_notification:
    :return:
    """
    try:
        await bot.send_message(user_id, text, disable_notification=disable_notification)
    except exceptions.BotBlocked:
        pass
    except exceptions.ChatNotFound:
        pass
    except exceptions.RetryAfter as e:
        await asyncio.sleep(e.timeout)
        return await send_message(user_id, text)  # Recursive call
    except exceptions.UserDeactivated:
        pass
    except exceptions.TelegramAPIError:
        pass
    else:
        pass
        return True
    return False


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
