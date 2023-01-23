from typing import Any

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton

from src.routing.menu import Menu


class NavigateBackCallback(CallbackData, prefix="back"):
    menu: Menu


class BackButton(InlineKeyboardButton):
    def __init__(self, menu: Menu):
        super().__init__(text="↩ Назад", callback_data=NavigateBackCallback(menu=menu).pack())
