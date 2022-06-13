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
