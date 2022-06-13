#!usr/bin/env python
"""
Name: server.py
Author: Hanich 5
Purpose: Main FastAPI entrypoint.
"""
import uvicorn
from fastapi import FastAPI

from classes.db_manager import DBManager
from utilities.database_constants import DatabaseConstants
from routers import hummus, user

APP = FastAPI()
APP.include_router(hummus.HUMMUS_ROUTES)
APP.include_router(user.USER_ROUTES)

DB_MANAGER = DBManager(DatabaseConstants.MONGO_URL)

if __name__ == '__main__':
    uvicorn.run(APP, host="127.0.0.1", port=8000)
