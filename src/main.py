from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from db.operations import check_if_user_in_db, add_user_to_db, check_if_user_is_admin, get_all_chat_ids

from handlers.register_handlers import register_all_handlers
from keyboards.main_menu_keyboard import main_menu_keyboard

BOT_TOKEN = "5077592058:AAGPmoUShW56UGfVxNGrJ8c0BNHRPqM98-w"

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
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

    await message.answer("Hi!", reply_markup=main_menu_keyboard)


@dp.message_handler(commands=['admin'])
async def admin(message: types.Message):
    """
    This handler will be called when user sends `/admin` command
    It will check if user is admin (in database) and call
    'Message for all' function
    """

    # TODO: create handler for message that will be sent to all users
    if check_if_user_is_admin(message.from_user.id):
        msg = "you are admin"
        for _id in get_all_chat_ids():
            await bot.send_message(_id, "Повідомлення для всіх")
    else:
        msg = "you are not admin"

    await message.reply(msg)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
