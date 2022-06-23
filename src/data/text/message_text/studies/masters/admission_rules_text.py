import json
from data.text.parser import replace_reserved_characters

masters_admission_rules_text = replace_reserved_characters(
    json.load(open("data/text/message_text/studies/masters/admission_rules.json", encoding="utf-8")))
