"""
Purpose: add item interface
Author: Hanich 02 (13.6.22)
"""
from pymongo import collection as mongo_collection


class IDbAdder:
    """
    interface of add item to collection
    """
    @staticmethod
    def add_item(item: dict, collection: mongo_collection):
        raise NotImplementedError
