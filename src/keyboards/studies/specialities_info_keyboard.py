from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.button_exit import button_exit
from data.text.button_text.text import common_button_text, speciality_info_button_text, bachelor_specialities_links


def get_speciality_info_keyboard(study_level: str, faculty: str, speciality: str):
    speciality_info_keyboard = InlineKeyboardMarkup(row_width=2)

    # TODO needs a lot of refactoring
    if study_level == "bachelors":
        general_info_button = InlineKeyboardButton(
            text=speciality_info_button_text["button_general_info"],
            callback_data="button_general_info"
        )
        speciality_info_keyboard.add(general_info_button)

        is_new_row = True
        for key in list(speciality_info_button_text.keys())[1:7]:
            button = InlineKeyboardButton(
                text=speciality_info_button_text[key],
                callback_data=key
            )
            if is_new_row:
                speciality_info_keyboard.add(button)
            else:
                speciality_info_keyboard.insert(button)
            is_new_row = not is_new_row

        for key in list(speciality_info_button_text.keys())[7:9]:
            button = InlineKeyboardButton(
                text=speciality_info_button_text[key],
                url=bachelor_specialities_links[faculty][speciality][key]
            )
            speciality_info_keyboard.add(button)

        # TODO change to a link button when provided a link
        youtube_button = InlineKeyboardButton(
            text=speciality_info_button_text["button_youtube"],
            callback_data=bachelor_specialities_links[faculty][speciality]["button_youtube"]
        )
        speciality_info_keyboard.add(youtube_button)

    button_back = InlineKeyboardButton(
        text=common_button_text["button_back"],
        callback_data="button_back"
    )

    speciality_info_keyboard.row(button_back, button_exit)
    return speciality_info_keyboard
