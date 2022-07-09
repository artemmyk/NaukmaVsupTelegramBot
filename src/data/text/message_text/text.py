import json
from data.text.parser import replace_reserved_characters

# text common to all menus
common_message_text = replace_reserved_characters(json.load(open("data/text/message_text/common.json", encoding="utf-8")))
basic_message_text = replace_reserved_characters(json.load(open("data/text/message_text/basic.json", encoding="utf-8")))
support_message_text = replace_reserved_characters(json.load(open("data/text/message_text/support.json", encoding="utf-8")))
