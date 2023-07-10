from dataclasses import dataclass

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.data.buttons import create_inline_button, EXIT
from src.data.speciality import Speciality
from src.routing.back_button import BackButton
from src.routing.menu import Menu


@dataclass
class Faculty:
    def __init__(self, callback_data, faculty_model: dict):
        self.callback_data = callback_data
        self.name = faculty_model["name"]

        specialities = list(faculty_model.items())[1:]
        self.specialities = [Speciality(callback_data, model) for callback_data, model in specialities]
        self.specialities_dict = {speciality.callback_data.name: speciality for speciality in self.specialities}

    @property
    def as_button(self) -> InlineKeyboardButton:
        return create_inline_button(self.name, callback_data=self.callback_data)

    @property
    def specialities_as_markup(self) -> InlineKeyboardMarkup:
        return InlineKeyboardBuilder(markup=[
            *[[speciality.as_button] for speciality in self.specialities],
            [BackButton(Menu.FACULTIES), EXIT]
        ]).as_markup()

    def get_speciality(self, name: str) -> Speciality:
        return self.specialities_dict[name]
