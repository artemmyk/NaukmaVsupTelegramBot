from typing import Optional

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from src.data.buttons import *
from src.routing.back_button import BackButton
from src.routing.main_menu import Degree
from src.routing.menu import Menu
from src.data.faculties import BACHELOR_FACULTIES, MASTER_FACULTIES

MAIN = ReplyKeyboardBuilder(markup=[
    [BACHELOR, MASTER],
    [ABOUT_UNIVERSITY, SUPPORT],
    [MEMES]
]).as_markup()

SPECIALITY = InlineKeyboardBuilder(markup=[
    [GENERAL_INFO],
    [DISCIPLINES, TEST],
    [STUDENTS_NUMBER, TUITION_COST],
    [KONKURS],
    [SITE],
    [BackButton(Menu.MAIN), EXIT]
]).as_markup()

ABOUT_UNIVERSITY = InlineKeyboardBuilder(markup=[
    [GENERAL_INFO],
    [STUDENT_ACTIVITY],
    [DORMITORIES],
    [STUDY_SYSTEM],
    [INFRASTRUCTURE],
    [EXIT]
]).as_markup()

SUPPORT = InlineKeyboardBuilder(markup=[
    [BackButton(Menu.MAIN), EXIT]
]).as_markup()

ABOUT_ACTIVITIES = InlineKeyboardBuilder(markup=[
    [ORGANISATIONS],
    [GOVERNMENT],
    [EVENTS],
    [PARTIES],
    [LIBRARIES],
    [BackButton(Menu.ABOUT_UNIVERSITY), EXIT]
]).as_markup()

INFRASTRUCTURE = InlineKeyboardBuilder(markup=[
    [CAMPUS],
    [WHERE_TO_EAT],
    [KMTS],
    [BackButton(Menu.ABOUT_UNIVERSITY), EXIT]
]).as_markup()

DEGREE = InlineKeyboardBuilder([
    [FACULTIES],
    [ADMISSION_RULES],
    [EXIT]
]).as_markup()

FINANCING_SOURCES = InlineKeyboardBuilder(markup=[
    [BUDGET, CONTRACT],
    [BackButton(Menu.ABOUT_UNIVERSITY)]
]).as_markup()

BACHELOR_FACULTIES = InlineKeyboardBuilder(markup=[
    *[[faculty.as_button] for faculty in BACHELOR_FACULTIES.values()],
    [BackButton(Menu.DEGREE), EXIT]]).as_markup()

MASTER_FACULTIES = InlineKeyboardBuilder(markup=[
    *[[faculty.as_button] for faculty in MASTER_FACULTIES.values()],
    [BackButton(Menu.DEGREE), EXIT]]).as_markup()

# admin keyboards
ADMIN = ReplyKeyboardBuilder(markup=[
    [ADD_MEME]
]).as_markup()

CANCEL = ReplyKeyboardBuilder(markup=[
    [CANCEL]
]).as_markup()
