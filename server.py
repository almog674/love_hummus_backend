#!usr/bin/env python
"""
Name: server.py
Author: Hanich 5
Purpose: Main FastAPI entrypoint.
"""
import uvicorn

from classes.database_manager import DBManager
from fastapi import FastAPI

from routers import hummus
from utilities.database_constants import DatabaseConstants

from fastapi.middleware.cors import CORSMiddleware

APP = FastAPI()
APP.include_router(hummus.HUMMUS_ROUTES)

origins = [
    "http://localhost:8000",
]

APP.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_MANAGER = DBManager(DatabaseConstants.MONGO_URL)

if __name__ == '__main__':
    uvicorn.run(APP, host="127.0.0.1", port=8000)
