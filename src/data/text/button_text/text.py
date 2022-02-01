import json

# text of buttons common to many keyboards
common_button_text = json.load(open("data/text/button_text/common.json", encoding="utf-8"))

# text of main menu buttons
main_menu_button_text = json.load(open("data/text/button_text/main_menu.json", encoding="utf-8"))

# text of faculties_menu buttons
faculties_button_text = json.load(open("data/text/button_text/studies/faculties.json", encoding="utf-8"))

# text of bachelor home buttons
bachelor_home_button_text = json.load(open("data/text/button_text/studies/bachelors/home.json", encoding="utf-8"))

# text of bachelor specialities_menu buttons
bachelor_specialities_button_text = json.load(
    open("data/text/button_text/studies/bachelors/specialities.json", encoding="utf-8"))

# text of bachelor speciality info
speciality_info_button_text = json.load(
    open("data/text/button_text/studies/bachelors/specialities_info.json", encoding="utf-8"))

# speciality info links
bachelor_specialities_links = json.load(
    open("data/text/button_text/studies/bachelors/links.json", encoding="utf-8"))
