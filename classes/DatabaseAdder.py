"""
Purpose: add item to database
Author: Hanich 02 (13.06.22)
"""

from interfaces.database_adding import IDbAdder
from pymongo import collection as mongo_collection


class DatabaseAdder(IDbAdder):
    """
    add item to database
    """
    @staticmethod
    def add_item(item: dict, collection: mongo_collection):
        collection.insertOne(item)