
ADMINS_IDS = [
    761303788
]


async def check_if_admin(chat_id):
    return chat_id in ADMINS_IDS
