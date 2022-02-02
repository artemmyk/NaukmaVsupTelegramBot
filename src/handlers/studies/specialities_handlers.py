from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from handlers.states import States
from data.text.message_text.text import common_message_text
from keyboards.studies.faculties_keyboard import faculties_keyboard
from keyboards.studies.specialities_info_keyboard import get_speciality_info_keyboard
from data.text.button_text.studies.studies_button_text import bachelor_specialities_menu_button_text


async def speciality_command(callback: CallbackQuery, state: FSMContext):
    speciality_name = callback.data.replace("button_", "")

    await States.next()

    async with state.proxy() as data:
        study_level = data["study_level"]
        faculty_name = data["faculty_name"]
        data["speciality_name"] = speciality_name

    await callback.message.delete()
    await callback.message.answer(
        common_message_text["choose_menu_item"],
        reply_markup=get_speciality_info_keyboard(study_level=study_level, faculty=faculty_name,
                                                  speciality=speciality_name)
    )
    await callback.answer()


async def back_command(callback: CallbackQuery):
    await States.previous()

    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"],
                                  reply_markup=faculties_keyboard)
    await callback.answer()


def register_handlers(dp: Dispatcher):
    for faculty in bachelor_specialities_menu_button_text.keys():
        for speciality_key in bachelor_specialities_menu_button_text[faculty].keys():
            dp.register_callback_query_handler(
                speciality_command,
                text=speciality_key,
                state=States.specialities_menu,
            )

    dp.register_callback_query_handler(
        back_command,
        text="button_back",
        state=States.specialities_menu,
    )
