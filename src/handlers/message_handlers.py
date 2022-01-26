from aiogram.dispatcher.filters import Text
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton

from main import dp








@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: Message):
    await message.answer("Що тебе цікавить?", reply_markup=keyboard)


@dp.message_handler(Text(equals='Бакалавр'))
async def bach(message: Message):
    await message.answer("Вибери пункт меню:", reply_markup=inline_keyboard_markup_1)


@dp.callback_query_handler(Text(equals="faculties"))
async def fac(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Вибери пункт меню:", reply_markup=inline_keyboard_markup_2)
    await callback.answer()


@dp.callback_query_handler(Text(equals="fen"))
async def fen(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("інфа про ФЕН")
    await callback.message.answer("Вибери пункт меню:", reply_markup=inline_keyboard_markup_2)
    await callback.answer()


@dp.callback_query_handler(Text(equals="fsnst"))
async def fsnst(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("інфа про ФСНСТ")
    await callback.message.answer("Вибери пункт меню:", reply_markup=inline_keyboard_markup_2)
    await callback.answer()


@dp.callback_query_handler(Text(equals="exit"))
async def fsnst(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Що тебе цікавить?", reply_markup=keyboard)


@dp.message_handler()
async def echo(message: Message):
    await message.answer('Я таке не знаю', reply_markup=keyboard)
