import random

FILE_IDS = [
    "AgACAgIAAxkBAAEcrPJj2tAaDX8lN30-iAg5IZuvxuq05wACw8gxGyWS2EpiniZ1XbMHQwEAAwIAA3kAAy4E",
]


def get_random_file_id():
    return random.choice(FILE_IDS)
