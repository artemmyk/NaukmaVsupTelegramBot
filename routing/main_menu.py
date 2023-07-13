from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

import data.buttons as buttons
import data.keyboards as keyboards
import data.memes as memes
from data.answers import BASIC, CHOOSE_MENU_ITEM
from functionality.util import handle_button

router = Router()


class State(StatesGroup):
    idle = State()
    bachelor = State()
    master = State()
    about_university = State()
    support = State()


async def admin(message: Message):
    return


@router.callback_query(handle_button(buttons.EXIT))
async def exit_to_main_menu(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(State.idle)
    await callback_query.message.answer(text=CHOOSE_MENU_ITEM, reply_markup=keyboards.MAIN)
    await callback_query.message.delete()


@router.message(Command(commands=['start', 'help']))
async def send_welcome(message: Message, state: FSMContext):
    await state.set_state(State.idle)
    await message.answer(BASIC["hey_there"], reply_markup=keyboards.MAIN)


@router.message(State.idle, Text(text=buttons.BACHELOR.text))
async def bachelor(message: Message, state: FSMContext):
    await state.set_state(State.bachelor)
    await message.answer(text=CHOOSE_MENU_ITEM, reply_markup=keyboards.DEGREE)


@router.message(State.idle, Text(text=buttons.MASTER.text))
async def master(message: Message, state: FSMContext):
    await state.set_state(State.master)
    await message.answer(text=CHOOSE_MENU_ITEM, reply_markup=keyboards.DEGREE)


@router.message(State.idle, Text(text=buttons.ABOUT_UNIVERSITY.text))
async def about_university(message: Message, state: FSMContext):
    await state.set_state(State.about_university)
    await message.answer(text=CHOOSE_MENU_ITEM, reply_markup=keyboards.ABOUT_UNIVERSITY)


@router.message(State.idle, Text(text=buttons.SUPPORT.text))
async def support(message: Message):
    await message.answer(text=CHOOSE_MENU_ITEM, reply_markup=keyboards.SUPPORT)


@router.message(State.idle, Text(text=buttons.MEMES.text))
async def meme(message: Message):
    await message.answer_photo(photo=memes.get_random_file_id(), reply_markup=keyboards.MAIN)


