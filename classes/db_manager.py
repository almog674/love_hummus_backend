"""
Name: db_manager.py
Author: Hanich 08
Purpose: Manages a mongo database, let you add, search or update
data there.
Date: 13/06/2022
"""

import pymongo

from utilities.database_constants import DatabaseConstants
from utilities.database_functions import DBFunctions
from classes import db_adder, db_updater, db_query


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
        self.available_functions = DBFunctions.FUNCTIONS_DICT
        self._db_adder = db_adder.DatabaseAdder()
        self._db_updater = db_updater.DatabaseUpdater()
        self._db_query = db_query.DatabaseQuery()
