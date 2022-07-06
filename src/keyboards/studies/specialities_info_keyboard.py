from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.common_buttons import button_back, button_exit
from data.text.button_text.studies.studies_button_text import speciality_info_menu_button_text, speciality_info_for_masters_menu_button_text
from data.text.message_text.studies.bachelors.specialities_info import bachelors_specialities_info_text
from data.text.message_text.studies.masters.specialities_info import masters_specialities_info_text


def get_speciality_info_keyboard(study_level: str, faculty: str, speciality: str):
    speciality_info_keyboard = InlineKeyboardMarkup(row_width=2)

    buttons = speciality_info_menu_button_text if study_level == "bachelors" else speciality_info_for_masters_menu_button_text
    amount_of_buttons = 7 if study_level == "bachelors" else 5

    general_info_button = InlineKeyboardButton(
        text=buttons["button_general_info"],
        callback_data="button_general_info"
    )
    speciality_info_keyboard.add(general_info_button)

    is_new_row = True
    for key in list(buttons.keys())[1:amount_of_buttons]:
        button = InlineKeyboardButton(
            text=buttons[key],
            callback_data=key
        )
        if is_new_row:
            speciality_info_keyboard.add(button)
        else:
            speciality_info_keyboard.insert(button)
        is_new_row = not is_new_row

    speciality_info_text = bachelors_specialities_info_text if study_level == "bachelors" else masters_specialities_info_text

    for key in list(buttons.keys())[amount_of_buttons:]:
        button = InlineKeyboardButton(
            text=buttons[key],
            url=speciality_info_text[faculty][speciality][key]
        )
        speciality_info_keyboard.add(button)

    speciality_info_keyboard.row(button_back, button_exit)
    return speciality_info_keyboard
