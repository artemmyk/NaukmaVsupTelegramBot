from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from handlers.states import States
from handlers.text import common_message_text
from keyboards.bachelors.faculties_keyboard import faculties_keyboard
from keyboards.text import bachelor_home_button_text


async def faculties_command(callback: CallbackQuery):
    await States.next()
    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"], reply_markup=faculties_keyboard)
    await callback.answer()


async def admission_rules_command(callback: CallbackQuery):
    pass
    # TODO


def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        faculties_command,
        state=States.bachelor_main,
        text="button_faculties"
    )
    dp.register_callback_query_handler(
        admission_rules_command,
        state=States.bachelor_main,
        text="button_admission_rules"
    )
