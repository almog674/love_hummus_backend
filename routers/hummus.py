#!usr/bin/env python
"""
Name: hummus.py
Author: Hanich 5
Purpose: Contain all hummus related routers.
"""
from fastapi import APIRouter, status
from uuid import UUID
from models import humusia_model, filter_model
from server import DB_MANAGER

HUMMUS_ROUTES = APIRouter()


@HUMMUS_ROUTES.post("/hummusiot/add", status_code=status.HTTP_201_CREATED)
async def add_hummusia(hummusia: humusia_model.HumusiaModel):
    """
    Adds the hummusia received from the body of the request to the database.
    """
    DB_MANAGER._db_adder.add_item(dict(hummusia), DB_MANAGER.humusiot_collection)
    return "Added"


@HUMMUS_ROUTES.put("/hummusiot/{hummusia_id}/{rating_given}")
async def add_rating_to_hummusia(hummusia_id: UUID, rating_given: int):
    """
    Updates the hummusia fields according to the rating given
    as a path parameter.
    """
    hummusia = DB_MANAGER._db_query.execute_query({"id": hummusia_id})[0]
    DB_MANAGER._db_updater.update_item(hummusia_id, {"rating_sum": hummusia["rating_sum"] + rating_given,
                                                     "number_of_ratings": hummusia["number_of_ratings"] + 1})
    return "updated"


@HUMMUS_ROUTES.get("/hummusiot/")
async def get_hummusia_by_filter(db_filter: filter_model):
    """
    Sends the user all hummsiot matching the given filter.
    """
    return DB_MANAGER._db_query.execute_query(db_filter.db_filter)
