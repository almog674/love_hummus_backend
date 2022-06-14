#!usr/bin/env python
"""
Name: database_manager_init.py
Author: Hanich 5
Purpose: Initiates an instance of the database manager.
Prevents a circular import by being in a seperate file.
"""
from classes import database_manager

DB_MANAGER = database_manager.DBManager("mongodb+srv://ron:almog@cluster0.a9tvj.mongodb.net/?retryWrites=true&w=majority")  # TODO: add a mongo
