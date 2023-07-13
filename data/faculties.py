from data.answers import BACHELOR_FACULTIES, MASTER_FACULTIES
from data.faculty import Faculty

BACHELOR_FACULTIES = {callback_data: Faculty(callback_data, model) for callback_data, model in BACHELOR_FACULTIES.items()}

MASTER_FACULTIES = {callback_data: Faculty(callback_data, model) for callback_data, model in MASTER_FACULTIES.items()}
