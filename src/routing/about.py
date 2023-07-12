from aiogram import Router
from aiogram.types import CallbackQuery

from src.data.answers import ABOUT_UNIVERSITY
from src.routing.main_menu import State
from src.routing.menu import Menu
import src.data.keyboards as kb

router = Router()

keyboards = {
    Menu.INFRASTRUCTURE: kb.INFRASTRUCTURE,
    Menu.FINANCING_SOURCES: kb.FINANCING_SOURCES,
}

@router.callback_query(State.about_university)
async def answer(callback_query: CallbackQuery):
    await callback_query.message.answer(ABOUT_UNIVERSITY[callback_query.data])
