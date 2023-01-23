from src.data.faculties import BACHELOR_FACULTIES, MASTER_FACULTIES

BACHELOR_SPECIALITIES = {faculty.callback_data: faculty.specialities for faculty in BACHELOR_FACULTIES}

MASTER_SPECIALITIES = {faculty.callback_data: faculty.specialities for faculty in MASTER_FACULTIES}