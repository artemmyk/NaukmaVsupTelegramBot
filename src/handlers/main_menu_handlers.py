from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from aiogram import Dispatcher

from handlers.states import States
from keyboards.bachelors.home_keyboard import home_keyboard
from keyboards.text import main_menu_button_text
from handlers.text import common_message_text


async def bachelor_command(message: Message):
    await States.bachelor_main.set()
    await message.answer(common_message_text["choose_menu_item"], reply_markup=home_keyboard)


async def masters_command(message: Message):
    pass
    # TODO


async def about_naukma_command(message: Message):
    pass
    # TODO


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(bachelor_command, Text(equals=main_menu_button_text["button_bachelors"]))
    dp.register_message_handler(masters_command, Text(equals=main_menu_button_text["button_masters"]))
    dp.register_message_handler(about_naukma_command, Text(equals=main_menu_button_text["button_about_naukma"]))
