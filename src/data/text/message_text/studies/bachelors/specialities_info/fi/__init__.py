import json
from data.text.parser import replace_reserved_characters

applied_math_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fi/applied_math.json", encoding="utf-8")))
cs_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fi/cs.json", encoding="utf-8")))
ipz_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fi/ipz.json", encoding="utf-8")))

fi_specialities_info = {
    "applied_math": applied_math_info,
    "cs": cs_info,
    "ipz": ipz_info
}
