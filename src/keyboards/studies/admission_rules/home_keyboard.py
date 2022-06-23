from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.common_buttons import button_back, button_exit
from data.text.button_text.studies.studies_button_text import admission_rules_main_menu_buttons_text
from data.text.message_text.studies.bachelors.admission_rules_text import bachelors_admission_rules_text


def get_home_keyboard():
    _home_keyboard = InlineKeyboardMarkup()

    for key in list(admission_rules_main_menu_buttons_text.keys())[0:-1]:
        button = InlineKeyboardButton(
            text=admission_rules_main_menu_buttons_text[key],
            callback_data=key
        )
        _home_keyboard.add(button)
    _home_keyboard.add(InlineKeyboardButton(
        text=admission_rules_main_menu_buttons_text["button_admission_commission_website"],
        url=bachelors_admission_rules_text["button_admission_commission_website"]
    ))
    _home_keyboard.row(button_back, button_exit)

    return _home_keyboard


admission_rules_home_keyboard = get_home_keyboard()
