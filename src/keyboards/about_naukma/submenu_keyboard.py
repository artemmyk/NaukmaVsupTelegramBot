from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.common_buttons import button_back, button_exit
from data.text.button_text.about_naukma.about_naukma_button_text import dormitories_menu_button_text, \
    infrastructure_menu_button_text, student_activity_menu_button_text


def get_submenu_keyboard(menu_button_text: dict):
    submenu_keyboard = InlineKeyboardMarkup()

    for key in menu_button_text.keys():
        button = InlineKeyboardButton(
            text=menu_button_text[key],
            callback_data=key
        )
        submenu_keyboard.add(button)

    submenu_keyboard.row(button_back, button_exit)

    return submenu_keyboard


def get_student_activity_menu_keyboard():
    return get_submenu_keyboard(student_activity_menu_button_text)


def get_infrastructure_menu_keyboard():
    return get_submenu_keyboard(infrastructure_menu_button_text)


def get_dormitories_menu_keyboard():
    return get_submenu_keyboard(dormitories_menu_button_text)
