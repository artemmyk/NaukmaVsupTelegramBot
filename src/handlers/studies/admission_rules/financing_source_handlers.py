from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from handlers.states import States
from data.text.message_text.text import common_message_text
from keyboards.studies.admission_rules.home_keyboard import admission_rules_home_keyboard
from data.text.button_text.studies.studies_button_text import financing_sources_menu_buttons_text
from data.text.message_text.studies.bachelors.admisson_rules_text import bachelors_admission_rules_text


async def financing_source_command(callback: CallbackQuery, state: FSMContext):
    financing_source = callback.data.replace("button_", "")

    async with state.proxy() as data:
        study_level = data["study_level"]
        admission_button = data["admission_button"]

    # TODO add masters
    admission_rules_text = bachelors_admission_rules_text if study_level == "bachelors" else bachelors_admission_rules_text

    await States.admission_rules_menu.set()

    await callback.message.delete()
    await callback.message.answer(admission_rules_text[admission_button][financing_source])
    await callback.message.answer(common_message_text["choose_menu_item"], reply_markup=admission_rules_home_keyboard)
    await callback.answer()


async def back_command(callback: CallbackQuery):
    await States.admission_rules_menu.set()
    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"], reply_markup=admission_rules_home_keyboard)
    await callback.answer()


def register_handlers(dp: Dispatcher):
    for key in financing_sources_menu_buttons_text.keys():
        dp.register_callback_query_handler(
            financing_source_command,
            text=key,
            state=States.financing_source_menu,
        )
    dp.register_callback_query_handler(
        back_command,
        text="button_back",
        state=States.financing_source_menu,
    )
