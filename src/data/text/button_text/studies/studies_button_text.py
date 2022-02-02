import json

# text of bachelor home buttons
home_menu_button_text = json.load(open("data/text/button_text/studies/home.json", encoding="utf-8"))

# text of faculties menu buttons
faculties_menu_button_text = json.load(open("data/text/button_text/studies/faculties.json", encoding="utf-8"))

# text of bachelor specialities_menu buttons
bachelor_specialities_menu_button_text = json.load(
    open("data/text/button_text/studies/bachelors/specialities.json", encoding="utf-8"))

# TODO add text of master's buttons

# text of speciality info
speciality_info_menu_button_text = json.load(
    open("data/text/button_text/studies/specialities_info.json", encoding="utf-8"))

# bachelor's specialities' info links
bachelor_specialities_links = json.load(
    open("data/text/button_text/studies/bachelors/links.json", encoding="utf-8"))

# TODO add links of master's buttons
