from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.common_buttons import button_back, button_exit
from data.text.button_text.studies.studies_button_text import faculties_menu_button_text


def get_faculties_keyboard():
    _faculties_keyboard = InlineKeyboardMarkup()

    for key in faculties_menu_button_text.keys():
        button = InlineKeyboardButton(
            text=faculties_menu_button_text[key],
            callback_data=key
        )
        _faculties_keyboard.add(button)

    _faculties_keyboard.row(button_back, button_exit)
    return _faculties_keyboard


faculties_keyboard = get_faculties_keyboard()
