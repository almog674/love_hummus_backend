"""
Name: humusia_model.py
Author: Hanich 08
Purpose: A model for holding all the required
data needed for humusia.
Date: 13/06/2022
"""

from pydantic import BaseModel, Field
import uuid
from datetime import time


class HumusiaModel(BaseModel):
    """
    This is a model for holding all the required
    data needed for humusia.
    """
    name: str = Field(max_length=40, description="The name of the humusia")
    city: str = Field(max_length=20,
                      description="The city which the humusia is located")
    rating_sum: int = 0
    number_of_ratings: int = 0
    open_time: str
    close_time: str
    price_class: str = Field(default="medium", description="Describes how expensive the hummus, can be low/medium/high")
    is_kosher: str = Field(default=False, description="Determine if the hummus is kosher.")
