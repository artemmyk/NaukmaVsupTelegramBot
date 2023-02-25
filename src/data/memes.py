import random

FILE_IDS = [
    "AgACAgIAAxkBAAEdqwxj-hrcmsFGIT5NkLbHXP6D8rJHdQACSc4xG70a0EvuuydLz97SJAEAAwIAA20AAy4E",
    "dsds",
    "dssf"
]


async def get_random_file_id():
    return random.choice(FILE_IDS)


async def remove_file_id(file_id):
    return FILE_IDS.remove(file_id)


async def add_file_id(file_id):
    return FILE_IDS.append(file_id)
