import json
from data.text.parser import replace_reserved_characters

culturology_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fhn/culturology.json", encoding="utf-8")))
history_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fhn/history.json", encoding="utf-8")))
philosophy_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fhn/philosophy.json", encoding="utf-8")))
german_philology_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fhn/german_philology.json", encoding="utf-8")))
ukrainian_philology_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fhn/ukrainian_philology.json", encoding="utf-8")))

fhn_specialities_info = {
    "culturology": culturology_info,
    "history": history_info,
    "philosophy": philosophy_info,
    "german_philology": german_philology_info,
    "ukrainian_philology": ukrainian_philology_info
}
