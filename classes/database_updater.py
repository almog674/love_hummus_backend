"""
Name: database_updater.py
Author: Hanich 08
Purpose: A class for updating data in a Mongodb collection.
Date: 13/06/2022
"""

import pymongo
from uuid import UUID

from utilities.outputMessages import SuccessMessages


class DatabaseUpdater:
    """
    A class for updating data in a Mongodb collection
    """

    @staticmethod
    def update_item(entry_name: str, new_values: dict, collection: pymongo.collection) -> str:
        collection.find_one_and_update({"name": entry_name}, new_values)
        return SuccessMessages.USER_UPDATED
