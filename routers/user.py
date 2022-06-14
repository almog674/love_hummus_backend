#!usr/bin/env python
"""
Name: user.py
Author: Hanich 5
Purpose: Contain all user related routers.
"""
from fastapi import APIRouter
from models import userModel
from database_manager_init import DB_MANAGER

USER_ROUTES = APIRouter()


@USER_ROUTES.post("/user/login")
async def login(user: userModel.UserModel):
    pass


@USER_ROUTES.post("/user/signup")
async def sign_up(user: userModel.UserModel):
    pass
