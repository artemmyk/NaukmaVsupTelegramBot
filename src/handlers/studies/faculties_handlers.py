from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from handlers.states import States
from data.text.message_text.text import common_message_text
from keyboards.studies.home_keyboard import get_home_keyboard
from keyboards.studies.specialities_keyboard import get_specialities_keyboard
from data.text.button_text.text import faculties_button_text


async def faculty_command(callback: CallbackQuery, state: FSMContext):
    faculty_name = callback.data.replace("button_", "")

    async with state.proxy() as data:
        study_level = data["study_level"]
        data["faculty_name"] = faculty_name

    await States.next()

    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"],
                                  reply_markup=get_specialities_keyboard(study_level, faculty_name))
    await callback.answer()


async def back_command(callback: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        study_level = data["study_level"]

    await States.previous()

    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"], reply_markup=get_home_keyboard(study_level))
    await callback.answer()


def register_handlers(dp: Dispatcher):
    for key in faculties_button_text.keys():
        dp.register_callback_query_handler(
            faculty_command,
            text=key,
            state=States.faculties_menu,
        )
    dp.register_callback_query_handler(
        back_command,
        text="button_back",
        state=States.faculties_menu,
    )
