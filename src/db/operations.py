from db.db_connection import get_collection
"""
This file implements different actions with database
"""


# function that checks whether user is in database
def check_if_user_in_db(chat_id):

    collection = get_collection()
    return collection is not None and collection.find_one({"chat_id": chat_id})


# function that checks whether user is admin
def check_if_user_is_admin(chat_id):
    collection = get_collection()
    return collection is not None and collection.find_one({"chat_id": chat_id, "admin": True})


# function that adds new document into database with given chat_id in it
def add_user_to_db(chat_id):
    collection = get_collection()
    if collection is not None:
        collection.insert_one({"chat_id": chat_id})


# function that returns all chat_id's from database (to send message to all users)
def get_all_chat_ids():
    collection = get_collection()
    if collection is not None:
        return [x["chat_id"] for x in collection.find({})]
