from aiogram import Dispatcher

from handlers import main_menu_handlers, common_handlers, basic_handlers
from handlers.support import support_handlers
from handlers.studies import studies_home_handlers, faculties_handlers, specialities_handlers, speciality_info_handlers
from handlers.studies.admission_rules import admission_rules_home_handlers, financing_source_handlers
from handlers.about_naukma import about_naukma_home_handlers, student_activity_handlers, dormitories_handlers, \
    infrastructure_handlers


def register_all_handlers(dp: Dispatcher):
    basic_handlers.register_handlers(dp)
    common_handlers.register_handlers(dp)
    main_menu_handlers.register_handlers(dp)
    support_handlers.register_handlers(dp)
    studies_home_handlers.register_handlers(dp)
    faculties_handlers.register_handlers(dp)
    specialities_handlers.register_handlers(dp)
    speciality_info_handlers.register_handlers(dp)
    admission_rules_home_handlers.register_handlers(dp)
    financing_source_handlers.register_handlers(dp)
    about_naukma_home_handlers.register_handlers(dp)
    student_activity_handlers.register_handlers(dp)
    dormitories_handlers.register_handlers(dp)
    infrastructure_handlers.register_handlers(dp)
