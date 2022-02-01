import json

international_relations_info = json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fsnst/international_relations.json", encoding="utf-8"))
politology_info = json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fsnst/politology.json", encoding="utf-8"))
psychology_info = json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fsnst/psychology.json", encoding="utf-8"))
public_relations_info = json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fsnst/public_relations.json", encoding="utf-8"))
social_work_info = json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fsnst/social_work.json", encoding="utf-8"))
sociology_info = json.load(
    open("data/text/message_text/studies/bachelors/specialities_info/fsnst/sociology.json", encoding="utf-8"))


fsnst_specialities_info = {
    "international_relations": international_relations_info,
    "politology": politology_info,
    "psychology": psychology_info,
    "public_relations": public_relations_info,
    "social_work": social_work_info,
    "sociology": sociology_info
}
