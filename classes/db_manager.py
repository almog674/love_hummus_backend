"""
Name: db_manager.py
Author: Hanich 08
Purpose: Manages a mongo database, let you add, search or update
data there.
Date: 13/06/2022
"""

import pymongo

from utilities.database_constants import DatabaseConstants


class DBManager:
    """
    Manages a mongo database, let you add, search or update
    data there.
    """

    def __init__(self, mongo_url: str):
        self.mongo_client = pymongo.MongoClient(mongo_url)
        self.database = self.mongo_client[DatabaseConstants.DATABASE_NAME]
        self.users_collection = self.database[DatabaseConstants.USERS_COLLECTION_NAME]
        self.humusiot_collection = self.database[DatabaseConstants.HUMUSIOT_COLLECTION_NAME]
