from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.button_exit import button_exit
from keyboards.text import common_button_text, speciality_info_button_text, bachelor_specialities_links


def get_speciality_info_keyboard(faculty: str, speciality: str):
    speciality_info_keyboard = InlineKeyboardMarkup(row_width=2)

    for key in list(speciality_info_button_text.keys())[:6]:
        button = InlineKeyboardButton(
            text=speciality_info_button_text[key],
            callback_data=key
        )
        speciality_info_keyboard.insert(button)
    for key in list(speciality_info_button_text.keys())[6:8]:
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
