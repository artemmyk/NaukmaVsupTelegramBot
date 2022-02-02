from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.common_buttons import button_back, button_exit
from data.text.button_text.studies.studies_button_text import bachelor_specialities_menu_button_text


def get_specialities_keyboard(study_level: str, faculty: str):
    specialities_keyboard = InlineKeyboardMarkup()

    # TODO change to masters home button text when there is one
    button_text = bachelor_specialities_menu_button_text if study_level == "bachelors" else bachelor_specialities_menu_button_text

    for key in button_text[faculty].keys():
        button = InlineKeyboardButton(
            text=button_text[faculty][key],
            callback_data=key
        )
        specialities_keyboard.add(button)

    specialities_keyboard.row(button_back, button_exit)
    return specialities_keyboard
