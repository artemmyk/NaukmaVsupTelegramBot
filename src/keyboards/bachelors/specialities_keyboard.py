from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.button_exit import button_exit
from keyboards.text import common_button_text, bachelor_specialities_button_text
from keyboards.callback_data import bachelor_specialities_callback_data


def get_specialities_keyboard(faculty: str):
    specialities_keyboard = InlineKeyboardMarkup()

    for key in bachelor_specialities_button_text[faculty].keys():
        button = InlineKeyboardButton(
            text=bachelor_specialities_button_text[faculty][key],
            callback_data=bachelor_specialities_callback_data[faculty][key]
        )
        specialities_keyboard.add(button)

    button_back = InlineKeyboardButton(
        text=common_button_text["button_back"],
        callback_data=bachelor_specialities_callback_data["button_back"]
    )

    specialities_keyboard.row(button_back, button_exit)
    return specialities_keyboard
