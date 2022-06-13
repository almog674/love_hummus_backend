"""
Purpose: execute query interface
Author: Hanich 02 (13.6.22)
"""
import collections


class IDbQuery:
    """
    interface of execute query from collection
    """
    @staticmethod
    def execute_query(item: dict, collection: collections.Collection) -> list:
        raise NotImplementedError
