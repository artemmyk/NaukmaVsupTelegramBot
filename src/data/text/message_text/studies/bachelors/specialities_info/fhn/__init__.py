import json

culturology_info = json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fhn/culturology.json", encoding="utf-8"))
history_info = json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fhn/history.json", encoding="utf-8"))
philosophy_info = json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fhn/philosophy.json", encoding="utf-8"))
german_philology_info = json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fhn/german_philology.json", encoding="utf-8"))
ukrainian_philology_info = json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fhn/ukrainian_philology.json", encoding="utf-8"))

fhn_specialities_info = {
    "culturology": culturology_info,
    "history": history_info,
    "philosophy": philosophy_info,
    "german_philology": german_philology_info,
    "ukrainian_philology": ukrainian_philology_info
}
