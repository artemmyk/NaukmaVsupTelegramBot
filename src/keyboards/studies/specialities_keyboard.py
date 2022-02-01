from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.button_exit import button_exit
from data.text.button_text.text import common_button_text, bachelor_specialities_button_text


def get_specialities_keyboard(study_level: str, faculty: str):
    specialities_keyboard = InlineKeyboardMarkup()

    # TODO change to masters home button text when there is one
    button_text = bachelor_specialities_button_text if study_level == "bachelors" else bachelor_specialities_button_text

    for key in button_text[faculty].keys():
        button = InlineKeyboardButton(
            text=button_text[faculty][key],
            callback_data=key
        )
        specialities_keyboard.add(button)

    button_back = InlineKeyboardButton(
        text=common_button_text["button_back"],
        callback_data="button_back"
    )

    specialities_keyboard.row(button_back, button_exit)
    return specialities_keyboard
