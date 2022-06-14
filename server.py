#!usr/bin/env python
"""
Name: server.py
Author: Hanich 5
Purpose: Main FastAPI entrypoint.
"""
import uvicorn
<<<<<<< HEAD
from routers import hummus
=======
from fastapi import FastAPI

from classes.db_manager import DBManager
from utilities.database_constants import DatabaseConstants
from routers import hummus, user
from classes import db_manager
>>>>>>> 5eff1a38d7158bbae509c9649acec1a78fb65aff

APP = FastAPI()
APP.include_router(hummus.HUMMUS_ROUTES)

DB_MANAGER = DBManager(DatabaseConstants.MONGO_URL)

if __name__ == '__main__':
    uvicorn.run(APP, host="127.0.0.1", port=8000)
