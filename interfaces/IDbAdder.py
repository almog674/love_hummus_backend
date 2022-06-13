"""
Purpose: add item interface
Author: Hanich 02 (13.6.22)
"""
import collections


class IDbAdder:
    """
    interface of add item to collection
    """
    @staticmethod
    def add_item(item: dict, collection: collections.Collection):
        raise NotImplementedError
