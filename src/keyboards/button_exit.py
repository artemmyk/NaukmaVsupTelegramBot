from aiogram.types import InlineKeyboardButton

from data.text.button_text.text import common_button_text

button_exit = InlineKeyboardButton(text=common_button_text["button_exit"],
                                   callback_data="button_exit")
