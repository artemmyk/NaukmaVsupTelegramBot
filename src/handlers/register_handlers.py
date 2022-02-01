from aiogram import Dispatcher

from handlers import main_menu_handlers, common_handlers
from handlers.studies import home_handlers, faculties_handlers, specialities_handlers, speciality_info_handlers


def register_all_handlers(dp: Dispatcher):
    common_handlers.register_handlers(dp)
    main_menu_handlers.register_handlers(dp)
    home_handlers.register_handlers(dp)
    faculties_handlers.register_handlers(dp)
    specialities_handlers.register_handlers(dp)
    speciality_info_handlers.register_handlers(dp)
