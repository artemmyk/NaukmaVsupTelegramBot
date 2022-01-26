from aiogram.types import InlineKeyboardButton

from keyboards.text import common_button_text
from keyboards.callback_data import common_callback_data

button_exit = InlineKeyboardButton(text=common_button_text["button_exit"],
                                   callback_data=common_callback_data["button_exit"])
