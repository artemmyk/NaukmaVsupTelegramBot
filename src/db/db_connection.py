from pymongo import MongoClient
import os
from dotenv import load_dotenv

"""
This file is responsible for connection to MongoDB
"""

load_dotenv()
CONNECTION_STRING = os.getenv("CONNECTION_STRING")


async def get_database():
    try:
        client = MongoClient(CONNECTION_STRING)
        return client.get_database("vstup_bot")
    except:
        print("Database connection failed")
        return None


async def get_collection():
    db = await get_database()
    if db is not None:
        return db["users"]
    return None
