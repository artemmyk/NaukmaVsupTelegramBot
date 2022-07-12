from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from data.text.message_text.text import common_message_text
from db.operations import check_if_user_in_db, add_user_to_db
from keyboards.main_menu_keyboard import main_menu_keyboard


# this command is registered only once as it works the same for all exit buttons
async def exit_command(callback: CallbackQuery, state: FSMContext):
    await state.finish()

    # check if user is in database (if not then add to db)
    if not await check_if_user_in_db(callback.message.from_user.id):
        await add_user_to_db(callback.message.from_user.id)

    await callback.message.delete()
    await callback.message.answer(common_message_text["what_are_you_interested_in"], reply_markup=main_menu_keyboard)
    await callback.answer()


def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(exit_command, text="button_exit", state="*")
