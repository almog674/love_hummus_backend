"""
Name: authenticator.py
Author: Hanich 08
Purpose: This class handle the authentication process, it helps you log into your user
or create new user.
Date: 13/06/2022
"""

from models.userModel import UserModel
from utilities.outputMessages import SuccessMessages
from classes.database_query import DatabaseQuery
from classes.db_adder import DatabaseAdder
from utilities.outputMessages import ErrorMessages
import pymongo


class Authenticator:
    """
    This class handle the authentication process, it helps you log into your user
    or create new user.
    """

    @staticmethod
    def signup(user_credentials: dict, users_collection: pymongo.collection):
        """
        :param user_credentials: The name & password of the user.
        :param users_collection: The collection of users.
        :return: Message which tells if the operation was a success
        """
        # TODO - Add error handling
        user_to_add = UserModel(name=user_credentials['name'], password=user_credentials['password'])
        DatabaseAdder.add_item(user_to_add.dict(), users_collection)
        return SuccessMessages.USER_CREATED

    def login(self, user_credentials: dict, users_collection: pymongo.collection):
        """
        :param user_credentials: The name & password of the user.
        :param users_collection: The collection of users.
        :return: Message which tells if the operation was a success
        """
        # Check user exist
        user = self.get_user_by_name(users_collection)
        if self.validate_user(user):
            if user['password'] != user_credentials['passowrd']:
                pass

        return user

    @staticmethod
    def get_user_by_name(name: str, users_collection: pymongo.collection):
        """
            :param name: The name of the user we want to get.
            :param users_collection: The collection of users.
        """
        user = DatabaseQuery.execute_query({"name": name}, users_collection)
        return user

    @staticmethod
    def validate_user(user_to_check: pymongo.cursor):
        """
            :param user_to_check: The user we want to validate.
        """
        is_user_valid = True
        if not user_to_check:
            print(ErrorMessages.USER_DOES_NOT_EXIST)
            is_user_valid = False
        return is_user_valid
