from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.button_exit import button_exit
from data.text.button_text.text import common_button_text, faculties_button_text


def get_faculties_keyboard():
    _faculties_keyboard = InlineKeyboardMarkup()

    for key in faculties_button_text.keys():
        button = InlineKeyboardButton(
            text=faculties_button_text[key],
            callback_data=key
        )
        _faculties_keyboard.add(button)

    button_back = InlineKeyboardButton(
        text=common_button_text["button_back"],
        callback_data="button_back"
    )

    _faculties_keyboard.row(button_back, button_exit)
    return _faculties_keyboard


faculties_keyboard = get_faculties_keyboard()
