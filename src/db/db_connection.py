from pymongo import MongoClient

"""
This file is responsible for connection to MongoDB
"""


def get_database():
    # TODO: hide connection string
    CONNECTION_STRING = "mongodb+srv://Vadym:1234@cluster0.0ljal.mongodb.net/vstup_bot?retryWrites=true&w=majority"

    try:
        client = MongoClient(CONNECTION_STRING)

        return client.get_database("vstup_bot")
    except:
        print("Database connection failed")
        return None


def get_collection():

    db = get_database()
    if db is not None:
        return db["users"]
    return None
