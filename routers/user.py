#!usr/bin/env python
"""
Name: user.py
Author: Hanich 5
Purpose: Contain all user related routers.
"""
from fastapi import APIRouter

USER_ROUTES = APIRouter()


@USER_ROUTES.post("/user/login")
async def login():
    pass


@USER_ROUTES.post("/user/signup")
async def login():
    pass
