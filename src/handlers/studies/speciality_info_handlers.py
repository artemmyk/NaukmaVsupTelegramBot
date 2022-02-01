from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from handlers.states import States
from data.text.message_text.text import common_message_text
from data.text.message_text.studies.bachelors.specialities_info import bachelors_specialities_info_text
from keyboards.studies.specialities_info_keyboard import get_speciality_info_keyboard
from keyboards.studies.specialities_keyboard import get_specialities_keyboard


async def get_info_command(button_pressed: str, callback: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        study_level = data["study_level"]
        faculty = data["faculty_name"]
        speciality = data["speciality_name"]

    # TODO change when masters info is added
    info_text = bachelors_specialities_info_text if study_level == "bachelors" else bachelors_specialities_info_text

    await callback.message.delete()
    await callback.message.answer(info_text[faculty][speciality][button_pressed])
    await callback.message.answer(common_message_text["choose_menu_item"],
                                  reply_markup=get_speciality_info_keyboard(study_level, faculty, speciality))
    await callback.answer()


async def general_info_command(callback: CallbackQuery, state: FSMContext):
    await get_info_command("button_general_info", callback, state)


async def disciplines_command(callback: CallbackQuery, state: FSMContext):
    await get_info_command("button_disciplines", callback, state)


async def zno_command(callback: CallbackQuery, state: FSMContext):
    await get_info_command("button_zno", callback, state)


async def students_number_command(callback: CallbackQuery, state: FSMContext):
    await get_info_command("button_students_number", callback, state)


async def cost_command(callback: CallbackQuery, state: FSMContext):
    await get_info_command("button_cost", callback, state)


async def score_needed_command(callback: CallbackQuery, state: FSMContext):
    await get_info_command("button_score_needed", callback, state)


async def count_score_command(callback: CallbackQuery, state: FSMContext):
    await get_info_command("button_count_score", callback, state)


async def back_command(callback: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        study_level = data["study_level"]
        faculty = data["faculty_name"]

    await States.previous()

    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"],
                                  reply_markup=get_specialities_keyboard(study_level, faculty))
    await callback.answer()


commands = {
  "button_general_info": general_info_command,
  "button_disciplines": disciplines_command,
  "button_zno": zno_command,
  "button_students_number": students_number_command,
  "button_cost": cost_command,
  "button_score_needed": score_needed_command,
  "button_count_score": count_score_command,
}


def register_handlers(dp: Dispatcher):
    for key in commands.keys():
        dp.register_callback_query_handler(
            commands[key],
            text=key,
            state=States.speciality_info_menu,
        )

    dp.register_callback_query_handler(
        back_command,
        text="button_back",
        state=States.speciality_info_menu,
    )
