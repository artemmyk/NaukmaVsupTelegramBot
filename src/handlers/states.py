from aiogram.dispatcher.filters.state import StatesGroup, State


class States(StatesGroup):
    studies_main_menu = State()
    faculties_menu = State()
    specialities_menu = State()
    speciality_info_menu = State()
