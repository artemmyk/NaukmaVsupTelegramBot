from db.db_connection import get_database
"""
This file implements different actions with database
"""
db = get_database()  # get database
collection = db["users"]


# function that checks whether user is in database
def check_if_user_in_db(chat_id):
    if collection.find_one({"chat_id": chat_id}):
        return True
    return False


# function that checks whether user is admin
def check_if_user_is_admin(chat_id):
    if collection.find_one({"chat_id": chat_id, "admin": True}):
        return True
    return False


# function that adds new document into database with given chat_id in it
def add_user_to_db(chat_id):
    collection.insert_one({"chat_id": chat_id})


# function that returns all chat_id's from database (to send message to all users)
def get_all_chat_ids():
    return [x["chat_id"] for x in collection.find({})]
