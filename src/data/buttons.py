from aiogram.types import InlineKeyboardButton, KeyboardButton


def create_keyboard_button(text: str) -> KeyboardButton:
    return KeyboardButton(text=text)


def create_inline_button(text: str, callback_data: str = None) -> InlineKeyboardButton:
    return InlineKeyboardButton(text=text, callback_data=callback_data)


EXIT: InlineKeyboardButton = create_inline_button("🚪 Вихід", "exit")

# MAIN MENU
BACHELOR: KeyboardButton = create_keyboard_button("Бакалавр")
MASTER: KeyboardButton = create_keyboard_button("Магістр")
ABOUT_UNIVERSITY: KeyboardButton = create_keyboard_button("Про Могилянку")
SUPPORT: KeyboardButton = create_keyboard_button("Підтримка")

# SPECIALTY INFO
GENERAL_INFO: InlineKeyboardButton = create_inline_button("Загальна інформація", "info")
DISCIPLINES: InlineKeyboardButton = create_inline_button("Предмети", "disciplines")
TEST: InlineKeyboardButton = create_inline_button("Вступний тест", "exam")
STUDENTS_NUMBER: InlineKeyboardButton = create_inline_button("Кількість місць", "number_of_students")
TUITION_COST: InlineKeyboardButton = create_inline_button("Вартість", "tuition_cost")
KONKURS: InlineKeyboardButton = create_inline_button("Перейти на konkurs.ukma", "konkurs")
SITE: InlineKeyboardButton = create_inline_button("Перейти на сайт спеціальності", "vstup")

# ABOUT UNIVERSITY
STUDENT_ACTIVITY: InlineKeyboardButton = create_inline_button("Студентські активності", "student_activity")
DORMITORIES: InlineKeyboardButton = create_inline_button("Гуртожитки", "dormitories")
STUDY_SYSTEM: InlineKeyboardButton = create_inline_button("Система навчання", "study_system")
INFRASTRUCTURE: InlineKeyboardButton = create_inline_button("Інфраструктура", "infrastructure")

# INFRASTRUCTURE
CAMPUS: InlineKeyboardButton = create_inline_button("Кампус", "campus")
WHERE_TO_EAT: InlineKeyboardButton = create_inline_button("Де поїсти?", "where_to_eat")
KMTS: InlineKeyboardButton = create_inline_button("КМЦ", "kmts")

# STUDENT ACTIVITIES
ORGANISATIONS: InlineKeyboardButton = create_inline_button("Організації", "organisations")
GOVERNMENT: InlineKeyboardButton = create_inline_button("Самоврядування", "government")
EVENTS: InlineKeyboardButton = create_inline_button("Події", "events")
PARTIES: InlineKeyboardButton = create_inline_button("Тусовки", "parties")
LIBRARIES: InlineKeyboardButton = create_inline_button("Бібліотеки", "libraries")

# DEGREE
FACULTIES: InlineKeyboardButton = create_inline_button("Факультети", "faculties")
ADMISSION_RULES: InlineKeyboardButton = create_inline_button("Правила вступу", "admission_rules")

# FINANCING SOURCES
BUDGET: InlineKeyboardButton = create_inline_button("Бюджет", "budget")
CONTRACT: InlineKeyboardButton = create_inline_button("Контракт", "contract")
