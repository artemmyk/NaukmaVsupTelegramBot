from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from data.text.message_text.about_naukma.about_naukma_text import home_message_text
from data.text.message_text.text import common_message_text
from handlers.states import States
from keyboards.about_naukma.home_keyboard import home_keyboard
from keyboards.about_naukma.submenu_keyboard import get_student_activity_menu_keyboard, \
    get_dormitories_menu_keyboard, get_infrastructure_menu_keyboard


async def general_info_command(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(home_message_text["button_general_info"])
    await callback.message.answer(common_message_text["choose_menu_item"], reply_markup=home_keyboard)
    await callback.answer()


async def student_activity_command(callback: CallbackQuery):
    await States.student_activity_menu.set()

    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"],
                                  reply_markup=get_student_activity_menu_keyboard())
    await callback.answer()


async def dormitories_command(callback: CallbackQuery):
    await States.dormitories_menu.set()

    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"],
                                  reply_markup=get_dormitories_menu_keyboard())
    await callback.answer()


async def study_system_command(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(home_message_text["button_study_system"])
    await callback.message.answer(common_message_text["choose_menu_item"], reply_markup=home_keyboard)
    await callback.answer()


async def infrastructure_command(callback: CallbackQuery):
    await States.infrastructure_menu.set()

    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"],
                                  reply_markup=get_infrastructure_menu_keyboard())
    await callback.answer()


commands = {
    "button_general_info": general_info_command,
    "button_student_activity": student_activity_command,
    "button_dormitories": dormitories_command,
    "button_study_system": study_system_command,
    "button_infrastructure": infrastructure_command
}


def register_handlers(dp: Dispatcher):
    for key in commands.keys():
        dp.register_callback_query_handler(
            commands[key],
            text=key,
            state=States.about_naukma_main_menu
        )
