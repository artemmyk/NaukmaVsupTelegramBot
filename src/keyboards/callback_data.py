import json

# callback data of buttons common to many keyboards
common_callback_data = json.load(open("data/callback_data/common.json", encoding="utf-8"))

# callback data of bachelor home buttons
bachelor_home_callback_data = json.load(open("data/callback_data/bachelors/home.json", encoding="utf-8"))

# callback data of bachelor faculties buttons
bachelor_faculties_callback_data = json.load(
    open("data/callback_data/bachelors/faculties.json", encoding="utf-8"))

# callback data of bachelor specialities buttons
bachelor_specialities_callback_data = json.load(
    open("data/callback_data/bachelors/specialities.json", encoding="utf-8"))

# callback data of bachelor speciality info buttons

bachelor_fen_specialities_info_callback_data = json.load(
    open("data/callback_data/bachelors/specialities_info/fen.json", encoding="utf-8"))
bachelor_fhn_specialities_info_callback_data = json.load(
    open("data/callback_data/bachelors/specialities_info/fhn.json", encoding="utf-8"))
bachelor_fi_specialities_info_callback_data = json.load(
    open("data/callback_data/bachelors/specialities_info/fi.json", encoding="utf-8"))
bachelor_fprn_specialities_info_callback_data = json.load(
    open("data/callback_data/bachelors/specialities_info/fprn.json", encoding="utf-8"))
bachelor_fpvn_specialities_info_callback_data = json.load(
    open("data/callback_data/bachelors/specialities_info/fpvn.json", encoding="utf-8"))
bachelor_fsnst_specialities_info_callback_data = json.load(
    open("data/callback_data/bachelors/specialities_info/fsnst.json", encoding="utf-8"))
