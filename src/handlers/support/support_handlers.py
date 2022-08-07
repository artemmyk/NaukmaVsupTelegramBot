import os

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, ContentTypes
from data.text.message_text.text import support_message_text, common_message_text
from dotenv import load_dotenv
from handlers.states import States
from keyboards.common_buttons import button_exit
from keyboards.main_menu_keyboard import main_menu_keyboard

load_dotenv()
CHAT_ID_FOR_BACHELORS = os.getenv("ADMINS_CHAT_ID_FOR_BACHELORS")
CHAT_ID_FOR_MASTERS = os.getenv("ADMINS_CHAT_ID_FOR_MASTERS")


async def get_study_level_command(callback: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["study_level"] = callback.data

    await callback.message.delete()
    await callback.message.answer(support_message_text["enter_your_question"],
                                  reply_markup=InlineKeyboardMarkup().add(button_exit))
    await callback.answer()


async def get_question_command(message: Message, state: FSMContext):
    async with state.proxy() as data:
        chat_id = int(CHAT_ID_FOR_BACHELORS if data["study_level"] == "bachelors" else CHAT_ID_FOR_MASTERS)
    if message.text is not None:
        await message.bot.send_message(chat_id=chat_id,
                                       text="№" + str(message.chat.id) + ";\n\n" +
                                            message.text,
                                       parse_mode="HTML")
    elif message.document is not None:
        await message.bot.send_document(chat_id=chat_id, document=message.document.file_id,
                                        caption="№" + str(message.chat.id) + ";\n\n" + (message.caption
                                        if message.caption is not None else "?"),
                                        parse_mode="HTML")
    await message.answer(support_message_text["thanks_for_question"])
    await message.answer(common_message_text["choose_menu_item"], reply_markup=main_menu_keyboard)
    await state.finish()


async def get_answer_command(message: Message):
    if message.text is not None:
        await message.bot.send_message(
            chat_id=int((message.reply_to_message.text if message.reply_to_message.text is not None
                         else message.reply_to_message.caption).split(";\n\n")[0][1:]),
            text=support_message_text["valid_answer_beginning"] +
                 (message.reply_to_message.text if message.reply_to_message.text is not None
                  else message.reply_to_message.caption).split(";\n\n")[1] +
                 support_message_text["valid_answer_end"] +
                 message.text, parse_mode="HTML"
        )
    elif message.document is not None:
        await message.bot.send_document(
            chat_id=int((message.reply_to_message.text if message.reply_to_message.text is not None
                         else message.reply_to_message.caption).split(";\n\n")[0][1:]),
            document=message.document.file_id,
            caption=support_message_text["valid_answer_beginning"] +
                    (message.reply_to_message.text if message.reply_to_message.text is not None
                     else message.reply_to_message.caption).split(";\n\n")[1]
                    + support_message_text["valid_answer_end"] +
                    (message.caption if message.caption is not None else ""), parse_mode="HTML"
        )


def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(get_study_level_command, state=States.support_main_menu)
    dp.register_message_handler(get_question_command, state=States.support_main_menu,
                                content_types=ContentTypes.DOCUMENT)
    dp.register_message_handler(get_question_command, state=States.support_main_menu,
                                content_types=ContentTypes.TEXT)
    dp.register_message_handler(get_answer_command, chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP],
                                is_reply=True, content_types=ContentTypes.DOCUMENT)
    dp.register_message_handler(get_answer_command, chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP],
                                is_reply=True, content_types=ContentTypes.TEXT)
