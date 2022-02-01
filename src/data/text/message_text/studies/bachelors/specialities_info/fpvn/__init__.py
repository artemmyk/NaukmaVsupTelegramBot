import json

government_info = json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fpvn/government.json", encoding="utf-8"))
law_info = json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fpvn/law.json", encoding="utf-8"))

fpvn_specialities_info = {
    "government": government_info,
    "law": law_info
}
