#!usr/bin/env python
"""
Name: server.py
Author: Hanich 5
Purpose: Main FastAPI entrypoint.
"""
from fastapi import FastAPI
import uvicorn

APP = FastAPI()


def main():
    pass


if __name__ == '__main__':
    uvicorn.run(APP, host="127.0.0.1", port=8000)
