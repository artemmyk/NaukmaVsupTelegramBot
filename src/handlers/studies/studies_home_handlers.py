from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from handlers.states import States
from data.text.message_text.text import common_message_text
from keyboards.studies.faculties_keyboard import faculties_keyboard
from keyboards.studies.admission_rules.home_keyboard import admission_rules_home_keyboard


async def faculties_command(callback: CallbackQuery):
    await States.next()
    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"], reply_markup=faculties_keyboard)
    await callback.answer()


async def admission_rules_command(callback: CallbackQuery):
    await States.admission_rules_menu.set()
    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"], reply_markup=admission_rules_home_keyboard)
    await callback.answer()


def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        faculties_command,
        state=States.studies_main_menu,
        text="button_faculties"
    )
    dp.register_callback_query_handler(
        admission_rules_command,
        state=States.studies_main_menu,
        text="button_admission_rules"
    )
