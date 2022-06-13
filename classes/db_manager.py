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

    @staticmethod
    def execute_database_function(self, command_name: str, command_arguments: str):
        pass