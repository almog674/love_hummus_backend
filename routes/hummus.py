#!usr/bin/env python
"""
Name: hummus.py
Author: Hanich 5
Purpose: Contain all hummus related routes.
"""
from fastapi import APIRouter

HUMMUS_ROUTES = APIRouter()


@HUMMUS_ROUTES.post("/hummusiot/add")
async def add_hummusia():
    pass