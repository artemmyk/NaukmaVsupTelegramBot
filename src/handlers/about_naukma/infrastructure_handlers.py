from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from data.text.message_text.about_naukma.about_naukma_text import infrastructure_message_text
from data.text.message_text.text import common_message_text
from handlers.states import States
from keyboards.about_naukma.home_keyboard import home_keyboard
from keyboards.about_naukma.submenu_keyboard import get_infrastructure_menu_keyboard


async def get_info_command(button_pressed: str, callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(infrastructure_message_text[button_pressed])
    await callback.message.answer(common_message_text["choose_menu_item"],
                                  reply_markup=get_infrastructure_menu_keyboard())
    await callback.answer()


async def campus_command(callback: CallbackQuery):
    await get_info_command("button_campus", callback)


async def where_to_eat_command(callback: CallbackQuery):
    await get_info_command("button_where_to_eat", callback)


async def working_spaces_command(callback: CallbackQuery):
    await get_info_command("button_working_spaces", callback)


async def kmts_command(callback: CallbackQuery):
    await get_info_command("button_kmts", callback)


async def back_command(callback: CallbackQuery):
    await States.previous()

    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"],
                                  reply_markup=home_keyboard)
    await callback.answer()


commands = {
  "button_campus": campus_command,
  "button_where_to_eat": where_to_eat_command,
  "button_working_spaces": working_spaces_command,
  "button_kmts": kmts_command
}


def register_handlers(dp: Dispatcher):
    for key in commands.keys():
        dp.register_callback_query_handler(
            commands[key],
            text=key,
            state=States.infrastructure_menu
        )

    dp.register_callback_query_handler(
        back_command,
        text="button_back",
        state=States.infrastructure_menu,
    )
