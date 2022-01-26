import json

# text of buttons common to many keyboards
common_button_text = json.load(open("data/text/button_text/common.json", encoding="utf-8"))

# text of main menu buttons
main_menu_button_text = json.load(open("data/text/button_text/main_menu.json", encoding="utf-8"))

# text of faculties buttons
faculties_button_text = json.load(open("data/text/button_text/faculties.json", encoding="utf-8"))

# text of bachelor home buttons
bachelor_home_button_text = json.load(open("data/text/button_text/bachelor_home.json", encoding="utf-8"))

# text of bachelor specialities buttons
bachelor_specialities_button_text = json.load(
    open("data/text/button_text/bachelor_specialities.json", encoding="utf-8"))

# text of bachelor speciality info
speciality_info_button_text = json.load(
    open("data/text/button_text/speciality_info.json", encoding="utf-8"))

# speciality info links
bachelor_fen_specialities_links = json.load(
    open("data/text/links/fen.json", encoding="utf-8"))
