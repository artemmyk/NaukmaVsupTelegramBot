from aiogram.types import InlineKeyboardButton

from data.text.button_text.general_button_text import common_button_text

button_exit = InlineKeyboardButton(text=common_button_text["button_exit"], callback_data="button_exit")
button_back = InlineKeyboardButton(text=common_button_text["button_back"], callback_data="button_back")
