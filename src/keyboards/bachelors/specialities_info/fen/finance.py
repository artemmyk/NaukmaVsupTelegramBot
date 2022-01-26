# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#
# from keyboards.button_exit import button_exit
# from keyboards.text import common_button_text, speciality_info_button_text, bachelor_fen_specialities_links
# from keyboards.callback_data import bachelor_fen_specialities_info_callback_data
#
# button_disciplines = InlineKeyboardButton(
#     text=speciality_info_button_text["button_disciplines"],
#     callback_data=bachelor_fen_specialities_info_callback_data["finance"]["button_disciplines"]
# )
# button_zno = InlineKeyboardButton(
#     text=speciality_info_button_text["button_zno"],
#     callback_data=bachelor_fen_specialities_info_callback_data["finance"]["button_zno"]
# )
# button_students_number = InlineKeyboardButton(
#     text=speciality_info_button_text["button_students_number"],
#     callback_data=bachelor_fen_specialities_info_callback_data["finance"]["button_students_number"]
# )
# button_cost = InlineKeyboardButton(
#     text=speciality_info_button_text["button_cost"],
#     callback_data=bachelor_fen_specialities_info_callback_data["finance"]["button_cost"]
# )
# button_score_needed = InlineKeyboardButton(
#     text=speciality_info_button_text["button_score_needed"],
#     callback_data=bachelor_fen_specialities_info_callback_data["finance"]["button_score_needed"]
# )
# button_count_score = InlineKeyboardButton(
#     text=speciality_info_button_text["button_count_score"],
#     callback_data=bachelor_fen_specialities_info_callback_data["finance"]["button_count_score"]
# )
# button_konkurs_ukma = InlineKeyboardButton(
#     text=speciality_info_button_text["button_konkurs_ukma"],
#     url=bachelor_fen_specialities_links["finance"]["button_konkurs_ukma"]
# )
# button_speciality_site = InlineKeyboardButton(
#     text=speciality_info_button_text["button_speciality_site"],
#     callback_data=bachelor_fen_specialities_links["finance"]["button_speciality_site"]
# )
# button_youtube = InlineKeyboardButton(
#     text=speciality_info_button_text["button_youtube"],
#     callback_data=bachelor_fen_specialities_links["finance"]["button_youtube"]
# )
# button_back = InlineKeyboardButton(
#     text=common_button_text["button_back"],
#     callback_data=bachelor_fen_specialities_info_callback_data["button_back"]
# )
#
# specialities_info = InlineKeyboardMarkup() \
#     .row(button_disciplines, button_zno) \
#     .row(button_students_number, button_cost) \
#     .row(button_score_needed, button_count_score) \
#     .add(button_konkurs_ukma) \
#     .add(button_speciality_site) \
#     .add(button_youtube) \
#     .row(button_back, button_exit)
