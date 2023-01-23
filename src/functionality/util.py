from typing import Optional

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, Update


# Return a single list from a list of lists.
def flatten(lst: list[list]):
    return [item for sublist in lst for item in sublist]


def button_labels_from_markup(markup: InlineKeyboardMarkup) -> list[str]:
    return list(map(lambda button: button.text, flatten(markup.inline_keyboard)))


def inline_buttons(inline_keyboard_markup: InlineKeyboardMarkup) -> list[InlineKeyboardMarkup]:
    return flatten(inline_keyboard_markup.inline_keyboard)


def callback_data_from_markup(markup: InlineKeyboardMarkup) -> set[str]:
    return set(map(lambda button: button.callback_data, flatten(markup.inline_keyboard)))


def handle_button(*buttons: InlineKeyboardButton):
    return lambda callback_query: any(map(lambda button: callback_query.data == button.callback_data, buttons))


def message_filter(button: KeyboardButton):
    return lambda text: button.text.casefold() == text
