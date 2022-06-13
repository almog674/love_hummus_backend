"""
Purpose: update item interface
Author: Hanich 02 (13.6.22)
"""
import collections


class DbUpdater:
    """
    interface of update item in collection
    """
    @staticmethod
    def update_item(new_values: dict, collection: collections.Collection):
        raise NotImplementedError
