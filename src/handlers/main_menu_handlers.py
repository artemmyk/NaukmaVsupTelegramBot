from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, InlineKeyboardMarkup
from data.text.button_text.general_button_text import main_menu_button_text
from data.text.message_text.text import common_message_text, support_message_text
from handlers.states import States
from keyboards.about_naukma.home_keyboard import about_naukma_home_keyboard
from keyboards.common_buttons import button_exit
from keyboards.studies.home_keyboard import studies_home_keyboard

from src.keyboards.support_keyboard import support_study_level_keyboard


async def bachelor_command(message: Message, state: FSMContext):
    await study_level_command("bachelors", message, state)


async def masters_command(message: Message, state: FSMContext):
    await study_level_command("masters", message, state)


async def study_level_command(study_level: str, message: Message, state: FSMContext):
    await States.studies_main_menu.set()

    async with state.proxy() as data:
        data["study_level"] = study_level

    await message.answer(common_message_text["choose_menu_item"], reply_markup=studies_home_keyboard)


async def about_naukma_command(message: Message):
    await States.about_naukma_main_menu.set()

    await message.answer(common_message_text["choose_menu_item"], reply_markup=about_naukma_home_keyboard)


async def support_command(message: Message):
    await States.support_main_menu.set()

    await message.answer(support_message_text["enter_your_question"],
                         reply_markup=support_study_level_keyboard)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(bachelor_command, Text(equals=main_menu_button_text["button_bachelors"]),
                                chat_type=[types.ChatType.PRIVATE])
    dp.register_message_handler(masters_command, Text(equals=main_menu_button_text["button_masters"]),
                                chat_type=[types.ChatType.PRIVATE])
    dp.register_message_handler(about_naukma_command, Text(equals=main_menu_button_text["button_about_naukma"]),
                                chat_type=[types.ChatType.PRIVATE])
    dp.register_message_handler(support_command, Text(equals=main_menu_button_text["button_support"]),
                                chat_type=[types.ChatType.PRIVATE])
