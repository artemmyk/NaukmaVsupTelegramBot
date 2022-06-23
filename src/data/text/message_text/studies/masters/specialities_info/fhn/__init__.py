import json
from data.text.parser import replace_reserved_characters

culturology_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fhn/culturology.json", encoding="utf-8")))
history_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fhn/history.json", encoding="utf-8")))
judaica_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fhn/judaica.json", encoding="utf-8")))
languages_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fhn/languages.json", encoding="utf-8")))
philology_literature_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fhn/philology_literature.json", encoding="utf-8")))
philology_ukrainian_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fhn/philology_ukrainian.json", encoding="utf-8")))
philosophy_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fhn/philosophy.json", encoding="utf-8")))

fhn_specialities_info = {
    "culturology": culturology_info,
    "history": history_info,
    "judaica": judaica_info,
    "languages": languages_info,
    "philology_literature": philology_literature_info,
    "philology_ukrainian": philology_ukrainian_info,
    "philosophy": philosophy_info,
}
