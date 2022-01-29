from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from handlers.states import States
from handlers.text import common_message_text
from keyboards.bachelors.home_keyboard import home_keyboard
from keyboards.bachelors.specialities_keyboard import get_specialities_keyboard
from keyboards.text import faculties_button_text


async def faculty_command(callback: CallbackQuery, state: FSMContext):
    faculty_name = callback.data.replace("button_", "")

    async with state.proxy() as data:
        data["faculty_name"] = faculty_name

    await States.next()

    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"],
                                  reply_markup=get_specialities_keyboard(faculty_name))
    await callback.answer()


async def back_command(callback: CallbackQuery):
    await States.previous()
    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"], reply_markup=home_keyboard)
    await callback.answer()


def register_handlers(dp: Dispatcher):
    for key in faculties_button_text.keys():
        dp.register_callback_query_handler(
            faculty_command,
            text=key,
            state=States.bachelor_faculties,
        )
    dp.register_callback_query_handler(
        back_command,
        text="button_back",
        state=States.bachelor_faculties,
    )
