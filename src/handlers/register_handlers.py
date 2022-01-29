from aiogram import Dispatcher

from handlers import main_menu_handlers, common_handlers
from handlers.bachelors import bachelors_home_handlers, bachelors_faculties_handlers, bachelors_specialities_handlers


def register_all_handlers(dp: Dispatcher):
    common_handlers.register_handlers(dp)
    main_menu_handlers.register_handlers(dp)
    bachelors_home_handlers.register_handlers(dp)
    bachelors_faculties_handlers.register_handlers(dp)
    bachelors_specialities_handlers.register_handlers(dp)
