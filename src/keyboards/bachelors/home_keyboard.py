from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.button_exit import button_exit
from keyboards.text import bachelor_home_button_text
from keyboards.callback_data import bachelor_home_callback_data


def get_home_keyboard():
    _home_keyboard = InlineKeyboardMarkup()

    for key in bachelor_home_button_text.keys():
        button = InlineKeyboardButton(
            text=bachelor_home_button_text[key],
            callback_data=bachelor_home_callback_data[key]
        )
        _home_keyboard.add(button)

    _home_keyboard.add(button_exit)
    return _home_keyboard


home_keyboard = get_home_keyboard()

# button_bachelor_faculties = InlineKeyboardButton(
#     text=bachelor_home_button_text["button_faculties"],
#     callback_data=bachelor_home_callback_data["button_faculties"]
# )
# button_bachelor_admission_rules = InlineKeyboardButton(
#     text=bachelor_home_button_text["button_admission_rules"],
#     callback_data=bachelor_home_callback_data["button_admission_rules"]
# )
#
# home_keyboard = InlineKeyboardMarkup() \
#     .add(button_bachelor_faculties) \
#     .add(button_bachelor_admission_rules) \
#     .add(button_exit)
