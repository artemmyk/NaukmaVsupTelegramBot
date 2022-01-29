from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from handlers.states import States
from handlers.text import common_message_text
from keyboards.bachelors.specialities_info_keyboard import get_speciality_info_keyboard
from keyboards.bachelors.specialities_keyboard import get_specialities_keyboard
from keyboards.text import bachelor_specialities_button_text, common_button_text


async def speciality_command(callback: CallbackQuery, state: FSMContext):
    speciality_name = callback.data.replace("button_", "")

    async with state.proxy() as data:
        data["speciality_name"] = speciality_name
        faculty_name = data["faculty_name"]

    await States.next()

    await callback.message.delete()
    await callback.message.answer(
        common_message_text["choose_menu_item"],
        reply_markup=get_speciality_info_keyboard(faculty=faculty_name, speciality=speciality_name)
    )
    await callback.answer()


async def back_command(callback: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        faculty_name = data["faculty_name"]

    await States.previous()

    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"],
                                  reply_markup=get_specialities_keyboard(faculty_name))
    await callback.answer()


def register_handlers(dp: Dispatcher):
    for faculty in bachelor_specialities_button_text.keys():
        for speciality_key in bachelor_specialities_button_text[faculty].keys():
            dp.register_callback_query_handler(
                speciality_command,
                text=speciality_key,
                state=States.bachelor_specialities,
            )

    dp.register_callback_query_handler(
        back_command,
        text=common_button_text["button_back"],
        state=States.bachelor_specialities,
    )
