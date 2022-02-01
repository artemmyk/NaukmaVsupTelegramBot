import json

economics_info = json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fen/economics.json", encoding="utf-8"))
finance_info = json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fen/finance.json", encoding="utf-8"))
management_info = json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fen/management.json", encoding="utf-8"))
marketing_info = json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fen/marketing.json", encoding="utf-8"))

fen_specialities_info = {
    "economics": economics_info,
    "finance": finance_info,
    "management": management_info,
    "marketing": marketing_info
}
