from enum import Enum


class Menu(str, Enum):
    MAIN = "main"
    SPECIALITY = "speciality",
    ABOUT_UNIVERSITY = "about_university"
    SUPPORT = "support"
    ABOUT_ACTIVITIES = "about_activities"
    INFRASTRUCTURE = "infrastructure"
    DEGREE = "degree"
    FACULTIES = "faculties"
    FINANCING_SOURCES = "financing_sources"
