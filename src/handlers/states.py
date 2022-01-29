from aiogram.dispatcher.filters.state import StatesGroup, State


class States(StatesGroup):
    bachelor_main = State()
    bachelor_faculties = State()
    bachelor_specialities = State()
    bachelor_speciality_info = State()
