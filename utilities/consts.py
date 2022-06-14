#!usr/bin/env python
"""
Name: consts.py
Author: Hanich 5
Purpose: Contain all consts.
"""


class HummusRouter:
    """
    Contains all consts related to hummus routers.
    """
    ONE_ID_PER_HUMMUSIA = 0
    INCREMENT_NUMBER_OF_RATINGS = 1


class UserReturnPrompts:
    """
    Contains all prompts returned to the user after
    his fullfiled request.
    """
    update_prompt = "Updated"
    add_prompt = "Added"
