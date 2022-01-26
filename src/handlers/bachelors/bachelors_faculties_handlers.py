from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from handlers.text import common_message_text
from keyboards.bachelors.home_keyboard import home_keyboard
from keyboards.bachelors.specialities_keyboard import get_specialities_keyboard
from keyboards.callback_data import bachelor_faculties_callback_data


async def fen_command(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"],
                                  reply_markup=get_specialities_keyboard("fen"))
    await callback.answer()


async def fsnst_command(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"],
                                  reply_markup=get_specialities_keyboard("fsnst"))
    await callback.answer()


async def fprn_command(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"],
                                  reply_markup=get_specialities_keyboard("fprn"))
    await callback.answer()


async def fpvn_command(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"],
                                  reply_markup=get_specialities_keyboard("fpvn"))
    await callback.answer()


async def fi_command(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"],
                                  reply_markup=get_specialities_keyboard("fi"))
    await callback.answer()


async def fhn_command(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"],
                                  reply_markup=get_specialities_keyboard("fhn"))
    await callback.answer()


async def back_command(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(common_message_text["choose_menu_item"], reply_markup=home_keyboard)
    await callback.answer()


def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(fen_command, text=bachelor_faculties_callback_data["button_fen"])
    dp.register_callback_query_handler(fsnst_command, text=bachelor_faculties_callback_data["button_fsnst"])
    dp.register_callback_query_handler(fprn_command, text=bachelor_faculties_callback_data["button_fprn"])
    dp.register_callback_query_handler(fpvn_command, text=bachelor_faculties_callback_data["button_fpvn"])
    dp.register_callback_query_handler(fi_command, text=bachelor_faculties_callback_data["button_fi"])
    dp.register_callback_query_handler(fhn_command, text=bachelor_faculties_callback_data["button_fhn"])

# def register_handlers(dp: Dispatcher):
#     for key in bachelor_specialities_button_text.keys():
#         async def command(callback: CallbackQuery):
#             await callback.message.delete()
#             await callback.message.answer(common_message_text["choose_menu_item"],
#                                           reply_markup=get_specialities_keyboard(key))
#             await callback.answer()
#
#         dp.register_callback_query_handler(command,
#                                            text=bachelor_faculties_callback_data["button_" + key])
#
#     dp.register_callback_query_handler(back_command, text=bachelor_faculties_callback_data["button_back"])
