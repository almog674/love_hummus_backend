#!usr/bin/env python
"""
Name: hummus.py
Author: Hanich 5
Purpose: Contain all hummus related routes.
"""
from fastapi import APIRouter, status
from uuid import UUID

HUMMUS_ROUTES = APIRouter()


@HUMMUS_ROUTES.post("/hummusiot/add", status_code=status.HTTP_201_CREATED)
async def add_hummusia():
    pass


@HUMMUS_ROUTES.put("/hummusiot/{hummusia_id}/{rating_given}")
async def add_rating_to_hummusia(hummusia_id: UUID, rating_given: int):
    pass


