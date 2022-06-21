from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.common_buttons import button_back, button_exit
from data.text.button_text.studies.studies_button_text import financing_sources_menu_buttons_text


def get_finance_source_keyboard():
    _keyboard = InlineKeyboardMarkup()

    for key in financing_sources_menu_buttons_text.keys():
        button = InlineKeyboardButton(
            text=financing_sources_menu_buttons_text[key],
            callback_data=key
        )
        _keyboard.row(button)
    _keyboard.row(button_back, button_exit)

    return _keyboard


financing_source_keyboard = get_finance_source_keyboard()
