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
    id: uuid.UUID = Field(default_factory=lambda: uuid.uuid4(),
                          description="The unique id of this humusia")
    name: str = Field(max_length=40, description="The name of the humusia")
    city: str = Field(max_length=20,
                      description="The city which the humusia is located")
    owner_id: uuid.UUID = Field(default="Unknown")
    rating_sum: int = 0
    number_of_ratings: int = 0
    open_time: time
    close_time: time
    price_class: str = Field(default="medium", description="Describes how expensive the hummus, can be low/medium/high")
    is_kosher: bool = Field(default=False,
                            description="Determine if the hummus is kosher.")
