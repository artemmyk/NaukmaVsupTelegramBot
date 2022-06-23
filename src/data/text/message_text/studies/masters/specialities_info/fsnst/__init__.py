import json
from data.text.parser import replace_reserved_characters


anticorruption_studies_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fsnst/anticorruption_studies.json", encoding="utf-8")))
international_relations_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fsnst/international_relations.json", encoding="utf-8")))
journalism_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fsnst/journalism.json", encoding="utf-8")))
politology_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fsnst/politology.json", encoding="utf-8")))
psychology_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fsnst/psychology.json", encoding="utf-8")))
public_relations_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fsnst/public_relations.json", encoding="utf-8")))
sociology_info = replace_reserved_characters(json.load(
    open("data/text/message_text/studies/masters/specialities_info/fsnst/sociology.json", encoding="utf-8")))


fsnst_specialities_info = {
    "anticorruption_studies": anticorruption_studies_info,
    "international_relations": international_relations_info,
    "journalism": journalism_info,
    "politology": politology_info,
    "psychology": psychology_info,
    "public_relations": public_relations_info,
    "sociology": sociology_info
}
