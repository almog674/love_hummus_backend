"""
Purpose: execute query interface
Author: Hanich 02 (13.6.22)
"""
from pymongo import collection as mongo_collection


class IDbQuery:
    """
    interface of execute query from collection
    """
    @staticmethod
    def execute_query(item: dict, collection: mongo_collection) -> list:
        raise NotImplementedError
