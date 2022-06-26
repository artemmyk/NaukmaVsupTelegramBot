from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from data.text.message_text.text import support_message_text, common_message_text
from handlers.states import States
from keyboards.main_menu_keyboard import main_menu_keyboard


async def get_question_command(message: Message, state: FSMContext):
    # TODO: add buddy chat id
    chat_id = -709588178

    try:
        await message.bot.forward_message(chat_id=chat_id, from_chat_id=message.chat.id, message_id=message.message_id)
    finally:
        await message.answer(support_message_text["thanks_for_question"], parse_mode="HTML")
    await message.answer(support_message_text["thanks_for_question"], parse_mode="HTML")
    await message.answer(common_message_text["choose_menu_item"], reply_markup=main_menu_keyboard)
    await state.finish()


async def get_answer_command(message: Message):
    await message.bot.send_message(chat_id=message.from_user.id,
                                   text=support_message_text["valid_answer_beginning"] + message.reply_to_message.text +
                                        support_message_text["valid_answer_end"] + message.text, parse_mode="HTML")
    await message.bot.delete_message(message_id=message.reply_to_message.message_id, chat_id=message.chat.id)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(get_question_command, state=States.support_main_menu)
    dp.register_message_handler(get_answer_command, chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP],
                                is_reply=True)
