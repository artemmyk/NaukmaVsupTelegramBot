from aiogram import Router
from aiogram.types import CallbackQuery

from data.answers import ABOUT_UNIVERSITY
from routing.main_menu import State
from routing.menu import Menu
import data.keyboards as kb

router = Router()

keyboards = {
    Menu.INFRASTRUCTURE: kb.INFRASTRUCTURE,
    Menu.FINANCING_SOURCES: kb.FINANCING_SOURCES,
}


@router.callback_query(State.about_university)
async def answer(callback_query: CallbackQuery):
    await callback_query.message.answer(ABOUT_UNIVERSITY[callback_query.data])
