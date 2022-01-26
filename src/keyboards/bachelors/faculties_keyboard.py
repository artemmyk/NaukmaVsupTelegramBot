from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.button_exit import button_exit
from keyboards.text import common_button_text, faculties_button_text
from keyboards.callback_data import bachelor_faculties_callback_data


def get_faculties_keyboard():
    _faculties_keyboard = InlineKeyboardMarkup()

    for key in faculties_button_text.keys():
        button = InlineKeyboardButton(
            text=faculties_button_text[key],
            callback_data=bachelor_faculties_callback_data[key]
        )
        _faculties_keyboard.add(button)

    button_back = InlineKeyboardButton(
        text=common_button_text["button_back"],
        callback_data=bachelor_faculties_callback_data["button_back"]
    )

    _faculties_keyboard.row(button_back, button_exit)
    return _faculties_keyboard


faculties_keyboard = get_faculties_keyboard()

# button_fen = InlineKeyboardButton(
#     text=faculties_button_text["button_fen"],
#     callback_data=bachelor_faculties_callback_data["button_fen"]
# )
# button_fsnst = InlineKeyboardButton(
#     text=faculties_button_text["button_fsnst"],
#     callback_data=bachelor_faculties_callback_data["button_fsnst"]
# )
# button_fprn = InlineKeyboardButton(
#     text=faculties_button_text["button_fprn"],
#     callback_data=bachelor_faculties_callback_data["button_fprn"]
# )
# button_fpvn = InlineKeyboardButton(
#     text=faculties_button_text["button_fpvn"],
#     callback_data=bachelor_faculties_callback_data["button_fpvn"]
# )
# button_fi = InlineKeyboardButton(
#     text=faculties_button_text["button_fi"],
#     callback_data=bachelor_faculties_callback_data["button_fi"]
# )
# button_fhn = InlineKeyboardButton(
#     text=faculties_button_text["button_fhn"],
#     callback_data=bachelor_faculties_callback_data["button_fhn"]
# )
# button_back = InlineKeyboardButton(
#     text=common_button_text["button_back"],
#     callback_data=bachelor_faculties_callback_data["button_back"]
# )
#
# specialities_info = InlineKeyboardMarkup() \
#     .add(button_fen) \
#     .add(button_fsnst) \
#     .add(button_fprn) \
#     .add(button_fpvn) \
#     .add(button_fi) \
#     .add(button_fhn) \
#     .row(button_back, button_exit)
