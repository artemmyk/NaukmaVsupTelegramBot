from aiogram.types import InlineKeyboardMarkup

from data.text.button_text.general_button_text import main_menu_button_text
from keyboards.common_buttons import button_exit

support_study_level_keyboard = InlineKeyboardMarkup().row(
                            InlineKeyboardMarkup(
                                 text=main_menu_button_text["button_bachelors"],
                                 callback_data="bachelors"
                             ),
                             InlineKeyboardMarkup(
                                 text=main_menu_button_text["button_masters"],
                                 callback_data="masters"
                             )).add(button_exit)