"""
Purpose: update item interface
Author: Hanich 02 (13.6.22)
"""
from pymongo import collection as mongo_collection


class DbUpdater:
    """
    interface of update item in collection
    """
    @staticmethod
    def update_item(new_values: dict, collection: mongo_collection):
        raise NotImplementedError
