from pymongo import MongoClient

"""
This file is responsible for connection to MongoDB
"""


def get_database():
    # TODO: hide connection string
    CONNECTION_STRING = "mongodb+srv://Vadym:1234@cluster0.0ljal.mongodb.net/vstup_bot?retryWrites=true&w=majority"

    client = MongoClient(CONNECTION_STRING)

    return client.get_database("vstup_bot")
