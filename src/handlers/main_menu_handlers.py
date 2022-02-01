from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from aiogram import Dispatcher

from handlers.states import States
from keyboards.studies.home_keyboard import get_home_keyboard
from data.text.button_text.text import main_menu_button_text
from data.text.message_text.text import common_message_text


async def bachelor_command(message: Message, state: FSMContext):
    await study_level_command("bachelors", message, state)


async def masters_command(message: Message, state: FSMContext):
    await study_level_command("masters", message, state)


async def study_level_command(study_level: str, message: Message, state: FSMContext):
    await States.studies_main_menu.set()

    async with state.proxy() as data:
        data["study_level"] = study_level

    await message.answer(common_message_text["choose_menu_item"], reply_markup=get_home_keyboard(study_level))


async def about_naukma_command(message: Message):
    pass
    # TODO


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(bachelor_command, Text(equals=main_menu_button_text["button_bachelors"]))
    dp.register_message_handler(masters_command, Text(equals=main_menu_button_text["button_masters"]))
    dp.register_message_handler(about_naukma_command, Text(equals=main_menu_button_text["button_about_naukma"]))
