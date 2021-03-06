"""
Name: outputMessages.py
Author: Hanich 08
Purpose: Keeps the output messages the api shows to the user.
Date: 13/06/2022
"""


class SuccessMessages:
    """
    Messages which tells the user his action was a success.
    """
    USER_CREATED = "User has created successfuly"
    USER_UPDATED = "User has updated successfuly"



class ErrorMessages:
    """
    Messages which helps the user understand what he did wrong
    and fix it
    """
    USER_DOES_NOT_EXIST = "The user you trying to connect to does not exist!"
    PASSWORD_NOT_MATCH = "The password in incorrect."
