#!usr/bin/env python
"""
Name: server.py
Author: Hanich 5
Purpose: Main FastAPI entrypoint.
"""
from fastapi import FastAPI
import uvicorn
from routers import hummus, user
from classes import database_manager

APP = FastAPI()
APP.include_router(hummus.HUMMUS_ROUTES)
# APP.include_router(user.USER_ROUTES)
DB_MANAGER = database_manager.DBManager("no")  # TODO: add a mongo

if __name__ == '__main__':
    uvicorn.run(APP, host="127.0.0.1", port=8000)
