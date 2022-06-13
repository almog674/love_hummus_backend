"""
Purpose: update item interface
Author: Hanich 02 (13.6.22)
"""
from pymongo import collection as mongo_collection
from uuid import UUID


class DbUpdater:
    """
    interface of update item in collection
    """

    @staticmethod
    def update_item(item_id: UUID, new_values: dict, collection: mongo_collection):
        raise NotImplementedError
