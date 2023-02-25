from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from aiogram import exceptions

from src.data import admin, keyboards, buttons, memes

router = Router()


class AdminState(StatesGroup):
    idle = State()
    add_meme = State()


@router.message(Command(commands=['admin']))
async def send_admin_welcome(message: Message, state: FSMContext):
    if await admin.check_if_admin(message.chat.id):
        await state.set_state(AdminState.idle)
        await message.answer("you're chosen", reply_markup=keyboards.ADMIN)


@router.message(AdminState.idle, Text(text=buttons.ADD_MEME.text))
async def add_meme(message: Message, state: FSMContext):
    await state.set_state(AdminState.add_meme)
    await message.answer(text="insert file_id", reply_markup=keyboards.CANCEL)


@router.message(Text(text=buttons.CANCEL.text))
async def cancel(message: Message, state: FSMContext):
    await state.set_state(AdminState.idle)
    await message.answer(text="you're still chosen", reply_markup=keyboards.ADMIN)


@router.message(AdminState.add_meme)
async def add_meme_again(message: Message):
    # TODO: test if valid image (try sending)
    await memes.add_file_id(message.text)
    await message.answer(text="meme added. insert file_id to add new meme", reply_markup=keyboards.CANCEL)
