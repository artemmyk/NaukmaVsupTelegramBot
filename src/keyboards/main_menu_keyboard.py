from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from data.text.button_text.text import main_menu_button_text

button_bachelors = KeyboardButton(main_menu_button_text["button_bachelors"])
button_masters = KeyboardButton(main_menu_button_text["button_masters"])
button_about_naukma = KeyboardButton(main_menu_button_text["button_about_naukma"])

main_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
main_menu_keyboard.row(button_bachelors, button_masters).add(button_about_naukma)
