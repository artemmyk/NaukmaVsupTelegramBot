from aiogram.types import InlineKeyboardButton

from keyboards.text import common_button_text

button_exit = InlineKeyboardButton(text=common_button_text["button_exit"],
                                   callback_data="button_exit")
