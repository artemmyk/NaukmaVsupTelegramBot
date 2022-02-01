import json

applied_math_info = json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fi/applied_math.json", encoding="utf-8"))
cs_info = json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fi/cs.json", encoding="utf-8"))
ipz_info = json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fi/ipz.json", encoding="utf-8"))

fi_specialities_info = {
    "applied_math": applied_math_info,
    "cs": cs_info,
    "ipz": ipz_info
}
