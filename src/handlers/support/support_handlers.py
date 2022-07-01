from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
import os
from dotenv import load_dotenv

from data.text.message_text.text import support_message_text, common_message_text
from handlers.states import States
from keyboards.main_menu_keyboard import main_menu_keyboard

load_dotenv()
CHAT_ID = os.getenv("ADMINS_CHAT_ID")


async def get_question_command(message: Message, state: FSMContext):
    await message.bot.send_message(chat_id=CHAT_ID, text=message.text + "\n\nchat_id: " + str(message.chat.id),
                                   parse_mode="HTML")
    await message.answer(support_message_text["thanks_for_question"])
    await message.answer(common_message_text["choose_menu_item"], reply_markup=main_menu_keyboard)
    await state.finish()


async def get_answer_command(message: Message):
    await message.bot.send_message(
        chat_id=int(message.reply_to_message.text.split("chat_id:")[1]),
        text=support_message_text["valid_answer_beginning"] +
             message.reply_to_message.text.split("\n\nchat_id:")[0] +
             support_message_text["valid_answer_end"] +
             message.text, parse_mode="HTML"
    )


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(get_question_command, state=States.support_main_menu)
    dp.register_message_handler(get_answer_command, chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP],
                                is_reply=True)
