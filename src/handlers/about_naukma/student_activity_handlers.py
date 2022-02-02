from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from data.text.message_text.about_naukma.about_naukma_text import student_activity_message_text
from data.text.message_text.text import common_message_text
from handlers.states import States
from keyboards.about_naukma.home_keyboard import home_keyboard
from keyboards.about_naukma.submenu_keyboard import get_student_activity_menu_keyboard


async def get_info_command(button_pressed: str, callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(student_activity_message_text[button_pressed])
    await callback.message.answer(common_message_text["choose_menu_item"],
                                  reply_markup=get_student_activity_menu_keyboard())
    await callback.answer()


async def organizations_command(callback: CallbackQuery):
    await get_info_command("button_organizations", callback)


async def student_government_command(callback: CallbackQuery):
    await get_info_command("button_student_government", callback)


async def events_command(callback: CallbackQuery):
    await get_info_command("button_events", callback)


async def parties_command(callback: CallbackQuery):
    await get_info_command("button_parties", callback)


async def best_place_command(callback: CallbackQuery):
    await get_info_command("button_best_place", callback)


async def back_command(callback: CallbackQuery):
    await States.previous()

    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"],
                                  reply_markup=home_keyboard)
    await callback.answer()


commands = {
    "button_organizations": organizations_command,
    "button_student_government": student_government_command,
    "button_events": events_command,
    "button_parties": parties_command,
    "button_best_place": best_place_command
}


def register_handlers(dp: Dispatcher):
    for key in commands.keys():
        dp.register_callback_query_handler(
            commands[key],
            text=key,
            state=States.student_activity_menu
        )

    dp.register_callback_query_handler(
        back_command,
        text="button_back",
        state=States.student_activity_menu,
    )
