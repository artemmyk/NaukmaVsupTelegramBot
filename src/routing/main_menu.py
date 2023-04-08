from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, FSInputFile

import src.data.buttons as buttons
import src.data.keyboards as keyboards
import src.data.memes as memes
from src.data.answers import BASIC, CHOOSE_MENU_ITEM
from src.functionality.util import handle_button

router = Router()


class Degree(StatesGroup):
    idle = State()
    bachelor = State()
    master = State()


async def admin(message: Message):
    return


@router.callback_query(handle_button(buttons.EXIT))
async def exit_to_main_menu(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(Degree.idle)
    await callback_query.message.answer(text=CHOOSE_MENU_ITEM, reply_markup=keyboards.MAIN)
    await callback_query.message.delete()


@router.message(Command(commands=['start', 'help']))
async def send_welcome(message: Message, state: FSMContext):
    await state.set_state(Degree.idle)
    await message.answer(BASIC["hey_there"], reply_markup=keyboards.MAIN)


@router.message(Degree.idle, Text(text=buttons.BACHELOR.text))
async def bachelor(message: Message, state: FSMContext):
    await state.set_state(Degree.bachelor)
    await message.answer(text=CHOOSE_MENU_ITEM, reply_markup=keyboards.DEGREE)


@router.message(Degree.idle, Text(text=buttons.MASTER.text))
async def master(message: Message, state: FSMContext):
    await state.set_state(Degree.master)
    await message.answer(text=CHOOSE_MENU_ITEM, reply_markup=keyboards.DEGREE)


@router.message(Degree.idle, Text(text=buttons.ABOUT_UNIVERSITY.text))
async def about_university(message: Message):
    await message.answer(text=CHOOSE_MENU_ITEM, reply_markup=keyboards.ABOUT_UNIVERSITY)


@router.message(Degree.idle, Text(text=buttons.SUPPORT.text))
async def support(message: Message):
    await message.answer(text=CHOOSE_MENU_ITEM, reply_markup=keyboards.SUPPORT)


@router.message(Degree.idle, Text(text=buttons.MEMES.text))
async def meme(message: Message):
    await message.answer_photo(photo=FSInputFile(memes.get_random_file()), reply_markup=keyboards.MAIN)


