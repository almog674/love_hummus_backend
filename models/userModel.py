"""
Name: userModel.py
Author: Hanich 08
Purpose: A model for holding all the required data for a user,
letting you create users in easy.
Date: 13/06/2022
"""

import uuid
from typing import List

from pydantic import BaseModel, Field


class UserModel(BaseModel):
    """
    A model for holding all the required data for a user,
    letting you create users in easy.
    """
    id: uuid.UUID = Field(default_factory=lambda: uuid.uuid4(),
                          description="The unique id of this user")
    name: str = Field(max_length=40, description="The name of the user")
    password: str
    owned_humusion: List[uuid.UUID] = []
