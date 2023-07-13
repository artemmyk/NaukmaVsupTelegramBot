import json

with open("data/answers.json", "r", encoding="utf-8") as file:
    ANSWERS: dict = json.load(file)

BASIC: dict = ANSWERS["basic"]

CHOOSE_MENU_ITEM = BASIC["choose_menu_item"]

BACHELOR: dict = ANSWERS["bachelor"]

BACHELOR_FACULTIES: dict = BACHELOR["faculties"]

MASTER: dict = ANSWERS["master"]

MASTER_FACULTIES: dict = MASTER["faculties"]

ABOUT_UNIVERSITY: dict = ANSWERS["about_university"]

SUPPORT: dict = ANSWERS["support"]
