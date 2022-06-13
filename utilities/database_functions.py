"""
Name: database_functions.py
Author: Hanich 02
Purpose: available functions in dictionary
Date: 13/06/2022
"""
from classes.db_updater import DatabaseUpdater


class DBFunctions:
    """
    dictionary of the available functions
    """
    FUNCTIONS_DICT = {"update": DatabaseUpdater.u, "add": print('add'), "execute": print('execute')}
