import json
from data.text.parser import replace_reserved_characters

government_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fpvn/government.json", encoding="utf-8")))
law_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fpvn/law.json", encoding="utf-8")))

fpvn_specialities_info = {
    "government": government_info,
    "law": law_info
}
