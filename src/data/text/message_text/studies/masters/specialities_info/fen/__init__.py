import json
from data.text.parser import replace_reserved_characters

business_info = replace_reserved_characters(
    json.load(open("data/text/message_text/studies/masters/specialities_info/fen/business.json", encoding="utf-8")))
economics_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fen/economics.json", encoding="utf-8")))
finance_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fen/finance.json", encoding="utf-8")))
management_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fen/management.json", encoding="utf-8")))
marketing_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fen/marketing.json", encoding="utf-8")))

fen_specialities_info = {
    "business": business_info,
    "economics": economics_info,
    "finance": finance_info,
    "management": management_info,
    "marketing": marketing_info
}
