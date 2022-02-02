from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.common_buttons import button_exit
from data.text.button_text.studies.studies_button_text import home_menu_button_text


def get_home_keyboard(study_level: str):
    _home_keyboard = InlineKeyboardMarkup()

    # TODO change to masters home button text when there is one
    button_text = home_menu_button_text if study_level == "bachelors" else home_menu_button_text

    for key in button_text.keys():
        button = InlineKeyboardButton(
            text=home_menu_button_text[key],
            callback_data=key
        )
        _home_keyboard.add(button)

    _home_keyboard.add(button_exit)
    return _home_keyboard
