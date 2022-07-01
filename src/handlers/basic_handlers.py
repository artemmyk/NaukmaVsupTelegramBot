from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import filters
from aiogram.utils import exceptions
import asyncio

from db.operations import check_if_user_in_db, add_user_to_db, check_if_user_is_admin, get_all_chat_ids
from data.text.message_text.text import basic_message_text
from keyboards.main_menu_keyboard import main_menu_keyboard


async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """

    # check if user is in database (if not then add to db)
    if not check_if_user_in_db(message.from_user.id):
        add_user_to_db(message.from_user.id)

    await message.answer(basic_message_text["hey_there"], reply_markup=main_menu_keyboard)


async def admin(message: types.Message):
    if check_if_user_is_admin(message.from_user.id):
        text = message.text.replace(basic_message_text["message_for_all_keycode"], "")

        for user_id in get_all_chat_ids():
            await send_message(message.bot, user_id, text)
            await asyncio.sleep(.05)


async def send_message(bot: Bot, user_id: int, text: str, disable_notification: bool = False) -> bool:
    """
    Safe messages sender
    :param bot:
    :param user_id:
    :param text:
    :param disable_notification:
    :return:
    """
    try:
        await bot.send_message(user_id, text, disable_notification=disable_notification)
    except exceptions.BotBlocked:
        print("Bot is blocked by ", user_id)
    except exceptions.ChatNotFound:
        print("Chat ", user_id, " is not found")
    except exceptions.RetryAfter as e:
        await asyncio.sleep(e.timeout)
        return await send_message(bot, user_id, text)  # Recursive call
    except exceptions.UserDeactivated:
        print(user_id, " is deactivated")
    except exceptions.TelegramAPIError:
        print("TelegramAPIError")
    else:
        print("some error")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start', 'help'], chat_type=[types.ChatType.PRIVATE], state="*")
    dp.register_message_handler(admin, filters.Text(contains=basic_message_text["message_for_all_keycode"]))
