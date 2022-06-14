#!usr/bin/env python
"""
Name: server.py
Author: Hanich 5
Purpose: Main FastAPI entrypoint.
"""
from fastapi import FastAPI
import uvicorn
from routers import hummus

APP = FastAPI()
APP.include_router(hummus.HUMMUS_ROUTES)

if __name__ == '__main__':
    uvicorn.run(APP, host="127.0.0.1", port=8000)
