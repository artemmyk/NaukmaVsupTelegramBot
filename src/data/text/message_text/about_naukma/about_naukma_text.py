import json
from data.text.parsing import replace_reserved_characters

# message text of about naukma home menu
home_message_text = replace_reserved_characters(json.load(open("data/text/message_text/about_naukma/home.json", encoding="utf-8")))

# message text of dormitories menu
dormitories_message_text = replace_reserved_characters(json.load(open("data/text/message_text/about_naukma/dormitories.json", encoding="utf-8")))

# message text of infrastructure menu
infrastructure_message_text = replace_reserved_characters(json.load(open("data/text/message_text/about_naukma/infrastructure.json", encoding="utf-8")))

# message text of student activity menu
student_activity_message_text = replace_reserved_characters(json.load(open("data/text/message_text/about_naukma/student_activity.json", encoding="utf-8")))
