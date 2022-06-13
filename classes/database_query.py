#!/usr/bin/env python
"""
Name: database_query.py
Author: Hanich 5
Purpose: Contains the implementation of an object that queries the database.
"""
from pymongo import collection as mongo_collection
from interfaces import database_excuting


class DatabaseQuery(database_excuting.IDbQuery):
    """
    Implementation of IDbQuery for mongoDB.
    """
    def execute_query(self, item: dict, collection: mongo_collection) -> list:
        """
        :param item: The query itself.
        :param collection: The collection to query.
        :return: Returns a list of all query results.
        """
        return collection.find(item)
