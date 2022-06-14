#!/usr/bin/env python
"""
Name: filter_model.py
Author: Hanich 5
Purpose: Contains a model for the database filter
"""
from pydantic import BaseModel


class DatabaseFilter(BaseModel):
    """
    A model for the filter received in the body of the request.
    """
    db_filter: dict
