"""
Name: userModel.py
Author: Hanich 08
Purpose: A model for holding all the required data for a user,
letting you create users in easy.
Date: 13/06/2022
"""

from pydantic import BaseModel, Field
import uuid


class UserModel(BaseModel):
    """
    A model for holding all the required data for a user,
    letting you create users in easy.
    """

