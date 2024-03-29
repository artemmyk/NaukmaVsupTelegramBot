from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from handlers.states import States
from data.text.message_text.text import common_message_text
from keyboards.studies.home_keyboard import get_home_keyboard
from keyboards.studies.admission_rules.home_keyboard import admission_rules_home_keyboard
from keyboards.studies.admission_rules.financing_source_keyboard import financing_source_keyboard
from data.text.button_text.studies.studies_button_text import admission_rules_main_menu_buttons_text
from data.text.message_text.studies.bachelors.admission_rules_text import bachelors_admission_rules_text
from data.text.message_text.studies.masters.admission_rules_text import masters_admission_rules_text


async def admission_menu_command(callback: CallbackQuery, state: FSMContext):
    button_name = callback.data

    async with state.proxy() as data:
        study_level = data["study_level"]
        data["admission_button"] = button_name

    admission_rules_text = bachelors_admission_rules_text if study_level == "bachelors" else masters_admission_rules_text

    await callback.message.delete()

    if button_name == list(admission_rules_main_menu_buttons_text.keys())[0] or button_name == \
            list(admission_rules_main_menu_buttons_text.keys())[1]:
        await States.financing_source_menu.set()
        await callback.message.answer(common_message_text["choose_menu_item"], reply_markup=financing_source_keyboard)
    else:
        await callback.message.answer(admission_rules_text[button_name])
        await callback.message.answer(common_message_text["choose_menu_item"],
                                      reply_markup=admission_rules_home_keyboard)

    await callback.answer()


async def back_command(callback: CallbackQuery, state: FSMContext):
    await States.studies_main_menu.set()

    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"], reply_markup=get_home_keyboard())
    await callback.answer()


def register_handlers(dp: Dispatcher):
    for key in admission_rules_main_menu_buttons_text.keys():
        dp.register_callback_query_handler(
            admission_menu_command,
            text=key,
            state=States.admission_rules_menu,
        )
    dp.register_callback_query_handler(
        back_command,
        text="button_back",
        state=States.admission_rules_menu,
    )
