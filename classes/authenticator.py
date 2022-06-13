"""
Name: authenticator.py
Author: Hanich 08
Purpose: This class handle the authentication process, it helps you log into your user
or create new user.
Date: 13/06/2022
"""

from models.userModel import UserModel
from utilities.outputMessages import SuccessMessages


class Authenticator:
    """
    This class handle the authentication process, it helps you log into your user
    or create new user.
    """

    @staticmethod
    def signup(user_credentials: dict):
        """
        :param user_credentials: The name & password of the user.
        :return:
        """
        # TODO - Add error handling
        UserModel(name=user_credentials['name'], password=user_credentials['password'])
        return SuccessMessages.USER_CREATED


