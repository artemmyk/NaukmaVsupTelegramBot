from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from handlers.text import common_message_text
from keyboards.callback_data import common_callback_data
from keyboards.callback_data import bachelor_home_callback_data
from keyboards.bachelors.faculties_keyboard import faculties_keyboard
from keyboards.main_menu_keyboard import main_menu_keyboard


async def faculties_command(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"], reply_markup=faculties_keyboard)
    await callback.answer()


async def admission_rules_command(callback: CallbackQuery):
    pass
    # TODO


# this command is registered only once as it works the same for all exit buttons
async def exit_command(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(common_message_text["what_are_interested_in"], reply_markup=main_menu_keyboard)
    await callback.answer()


def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(faculties_command, text=bachelor_home_callback_data["button_faculties"])
    dp.register_callback_query_handler(admission_rules_command,
                                       text=bachelor_home_callback_data["button_admission_rules"])
    dp.register_callback_query_handler(exit_command, text=common_callback_data["button_exit"])
