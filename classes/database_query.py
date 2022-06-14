#!/usr/bin/env python
"""
Name: database_query.py
Author: Hanich 5
Purpose: Contains the implementation of an object that queries the database.
"""
from pymongo import collection as mongo_collection
from pymongo.cursor import Cursor
from interfaces import database_excuting


class DatabaseQuery(database_excuting.IDbQuery):
    """
    Implementation of IDbQuery for mongoDB.
    """

    @staticmethod
    def create_list_from_cursor(entries_cursor=Cursor) -> list:
        """
         :param entries_cursor: The cursor of the entries we had found with the filter.
         :return: A list of all the entries.
        """
        entries_found = []
        for entry in entries_cursor:
            entries_found.append(entry)
        return entries_found

    def execute_query(self, db_filter: dict, collection: mongo_collection) -> list:
        """
        :param db_filter: The filter we use to query the entries.
        :param collection: The collection to query.
        :return: Returns a list of all query results.
        """
        entries_cursor = collection.find(db_filter, {'_id': 0})
        entries_list = self.create_list_from_cursor(entries_cursor)
        return entries_list
