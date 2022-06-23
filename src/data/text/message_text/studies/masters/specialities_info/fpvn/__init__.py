import json
from data.text.parser import replace_reserved_characters

law_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fpvn/law.json", encoding="utf-8")))
social_politics_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fpvn/social_politics.json", encoding="utf-8")))

fpvn_specialities_info = {
    "law": law_info,
    "social_politics": social_politics_info
}
