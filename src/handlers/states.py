from aiogram.dispatcher.filters.state import StatesGroup, State


class States(StatesGroup):
    studies_main_menu = State()
    faculties_menu = State()
    specialities_menu = State()
    speciality_info_menu = State()
    asking_for_grades = State()
    admission_rules_menu = State()
    financing_source_menu = State()
    about_naukma_main_menu = State()
    support_main_menu = State()
    student_activity_menu = State()
    dormitories_menu = State()
    infrastructure_menu = State()
    support_menu = State()
