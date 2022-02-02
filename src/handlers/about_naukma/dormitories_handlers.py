from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from data.text.message_text.about_naukma.about_naukma_text import dormitories_message_text
from data.text.message_text.text import common_message_text
from handlers.states import States
from keyboards.about_naukma.home_keyboard import home_keyboard
from keyboards.about_naukma.submenu_keyboard import get_dormitories_menu_keyboard


async def get_info_command(button_pressed: str, callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(dormitories_message_text[button_pressed])
    await callback.message.answer(common_message_text["choose_menu_item"],
                                  reply_markup=get_dormitories_menu_keyboard())
    await callback.answer()


async def settlement_process_command(callback: CallbackQuery):
    await get_info_command("button_settlement_process", callback)


async def dormitory_cost_command(callback: CallbackQuery):
    await get_info_command("button_dormitory_cost", callback)


async def settlement_privileges_command(callback: CallbackQuery):
    await get_info_command("button_settlement_privileges", callback)


async def settlement_documents_command(callback: CallbackQuery):
    await get_info_command("button_settlement_documents", callback)


async def dormitories_infrastructure_command(callback: CallbackQuery):
    await get_info_command("button_dormitories_infrastructure", callback)


async def back_command(callback: CallbackQuery):
    await States.previous()

    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"],
                                  reply_markup=home_keyboard)
    await callback.answer()


commands = {
  "button_settlement_process": settlement_process_command,
  "button_dormitory_cost": dormitory_cost_command,
  "button_settlement_privileges": settlement_privileges_command,
  "button_settlement_documents": settlement_documents_command,
  "button_dormitories_infrastructure": dormitories_infrastructure_command
}


def register_handlers(dp: Dispatcher):
    for key in commands.keys():
        dp.register_callback_query_handler(
            commands[key],
            text=key,
            state=States.dormitories_menu
        )

    dp.register_callback_query_handler(
        back_command,
        text="button_back",
        state=States.dormitories_menu,
    )
