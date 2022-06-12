import json
from data.text.parser import replace_reserved_characters

bio_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fprn/bio.json", encoding="utf-8")))
chemistry_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fprn/chemistry.json", encoding="utf-8")))
ecology_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fprn/ecology.json", encoding="utf-8")))
physics_astronomy_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fprn/physics_astronomy.json", encoding="utf-8")))

fprn_specialities_info = {
    "bio": bio_info,
    "chemistry": chemistry_info,
    "ecology": ecology_info,
    "physics_astronomy": physics_astronomy_info
}
