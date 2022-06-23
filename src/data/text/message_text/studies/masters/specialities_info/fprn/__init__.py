import json
from data.text.parser import replace_reserved_characters

chemistry_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fprn/chemistry.json", encoding="utf-8")))
ecology_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fprn/ecology.json", encoding="utf-8")))
lab_diagnostics_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fprn/lab_diagnostics.json", encoding="utf-8")))
molecular_biology_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fprn/molecular_biology.json", encoding="utf-8")))
physics_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fprn/physics.json", encoding="utf-8")))

fprn_specialities_info = {
    "chemistry": chemistry_info,
    "ecology": ecology_info,
    "lab_diagnostics": lab_diagnostics_info,
    "molecular_biology": molecular_biology_info,
    "physics_astronomy": physics_info
}
