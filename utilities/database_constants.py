"""
Name: database_constants.py
Author: Hanich 08
Purpose: Keep constants relevant to the database usage.
Date: 13/06/2022
"""


class DatabaseConstants:
    """
    Constants for the connection to the database
    """
    MONGO_URL = "mongodb://127.0.0.1:27017/"
    DATABASE_NAME = "humusiat_ron_ubanav"
    USERS_COLLECTION_NAME = "users"
    HUMUSIOT_COLLECTION_NAME = "humusiot"
