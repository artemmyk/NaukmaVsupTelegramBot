from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.button_exit import button_exit
from keyboards.text import bachelor_home_button_text


def get_home_keyboard():
    _home_keyboard = InlineKeyboardMarkup()

    for key in bachelor_home_button_text.keys():
        button = InlineKeyboardButton(
            text=bachelor_home_button_text[key],
            callback_data=key
        )
        _home_keyboard.add(button)

    _home_keyboard.add(button_exit)
    return _home_keyboard


home_keyboard = get_home_keyboard()
