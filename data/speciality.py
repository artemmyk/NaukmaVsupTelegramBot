from dataclasses import dataclass

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton

from data.buttons import create_inline_button


class SpecialityCallback(CallbackData, prefix="speciality"):
    name: str


@dataclass
class Speciality:
    def __init__(self, callback_data: str, speciality_model: dict):
        self.callback_data = SpecialityCallback(name=callback_data)

        for category in speciality_model:
            speciality_model[category] = to_markdown(speciality_model[category])

        self.name = speciality_model["name"]
        self.info = speciality_model["info"]
        self.disciplines = speciality_model["disciplines"]
        self.exam = speciality_model["exam"]
        self.number_of_students = speciality_model["number_of_students"]
        self.tuition_cost = speciality_model["tuition_cost"]
        self.score_needed = speciality_model["score_needed"]
        self.konkurs = speciality_model["konkurs"]
        self.vstup = speciality_model["vstup"]

    @property
    def as_button(self) -> InlineKeyboardButton:
        return create_inline_button(self.name, callback_data=self.callback_data.pack())


def to_markdown(string: str) -> str:
    if string.startswith("https"):
        return string
    return string.replace("[сайт приймальної комісії НаУКМА]<@https://vstup.ukma.edu.ua/golovna/pryjmalna-komisiya/@>",
                          "[сайт]<@https://vstup.ukma.edu.ua/@> приймальної комісії НаУКМА") \
        .replace("https://vstup.ukma.edu.ua/wp-content/uploads/2022/05/motyvaciyniy_lyst_2022.pdf",
                 "https://vstup.ukma.edu.ua/bachelor/motyvaciyniy-lyst-2022") \
        .replace("МТНК(магістерський тест навчальної компетентності) та фаховий іспит",
                 "МТНК(магістерський тест навчальної компетентності) та фаховий іспит (детальніше [тут]<@https://vstup.ukma.edu.ua/master-degree/mkt-mtnk@>)") \
        .replace("на сайті НаУКМА", "на сайті Могилянки") \
        .replace(".", "\\.") \
        .replace(",", "\\,").replace(";", "\\;").replace("(", "\\(").replace(")", "\\)") \
        .replace("!", "\\!").replace("?", "\\?").replace("-", "\\-").replace("<@", "(").replace("@>", ")")
