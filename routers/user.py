#!usr/bin/env python
"""
Name: user.py
Author: Hanich 5
Purpose: Contain all user related routers.
"""
from fastapi import APIRouter
from classes.db_manager import DBManager
from models import userModel
from server import DB_MANAGER

USER_ROUTES = APIRouter()


@USER_ROUTES.post("/user/login")
async def login(user_credentials: dict):
    database_manager = DBManager()
    results = database_manager.execute_database_function("login", user_credentials)
    return results


@USER_ROUTES.post("/user/signup")
async def signup():
    async def login(user: userModel.UserModel):
        pass


@USER_ROUTES.post("/user/signup")
async def sign_up(user: userModel.UserModel):
    pass
