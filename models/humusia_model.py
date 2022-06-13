"""
Name: humusia_model.py
Author: Hanich 08
Porpuse: 
Date: 13/06/2022
"""

from pydantic import BaseModel, Field
from uuid import uuid4


class HumusiaModel(BaseModel):
    """
    This is a model for holding all the required
    data needed for humusia.
    """
    id: Field(default_factory=lambda: uuid4(),
              description="The unique id of this humusia")
    name: str = Field(max_length=40, description="The name of the humusia")
    city: str = Field(max_length=20,
                      description="The city which the humusia is located")
    # TODO - change it to user
    owner: str = Field(default="Unknown")
    rating_sun: int = 0
    number_of_ratings: int = 0
    price_class: str = Field(default="medium")