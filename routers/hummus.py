#!usr/bin/env python
"""
Name: hummus.py
Author: Hanich 5
Purpose: Contain all hummus related routers.
"""
from fastapi import APIRouter, status
from uuid import UUID
from models import humusia_model, filter_model
from database_manager_init import DB_MANAGER
from utilities.consts import HummusRouter, UserReturnPrompts

HUMMUS_ROUTES = APIRouter()


@HUMMUS_ROUTES.post("/hummusiot/add", status_code=status.HTTP_201_CREATED)
async def add_hummusia(hummusia: humusia_model.HumusiaModel):
    """
    Adds the hummusia he received from the body of the request to the database.
    :param hummusia: A json with all the fields neccesery for the humusia model.

    Example: {
    "name": "name",
    "city": "city",
    "is_kosher": "true",
    "open_hour": "13:30",
    "close_hour": "16:30"
    }

    Returns a string which tells if the action was a success
    """
    DB_MANAGER._db_adder.add_item(dict(hummusia), DB_MANAGER.humusiot_collection)
    return UserReturnPrompts.add_prompt


@HUMMUS_ROUTES.put("/hummusiot/{hummusia_id}/{rating_given}")
async def add_rating_to_hummusia(hummusia_id: UUID, rating_given: int):
    """
    Updates the hummusia fields according to the rating given
    as a path parameter.

    :param hummusia_id: The id of the hummusia we want to rate.
    :param rating_given: the rating we want to give to the hummusia

    Example:
    /hummusiot/12523753285232/4.7

    Returns a string which tells if the action was a success
    """
    hummusia = DB_MANAGER._db_query.execute_query({"id": hummusia_id})[HummusRouter.ONE_ID_PER_HUMMUSIA]
    DB_MANAGER._db_updater.update_item(hummusia_id,
                                       {"rating_sum": hummusia["rating_sum"] + rating_given,
                                        "number_of_ratings": hummusia[
                                         "number_of_ratings"] + HummusRouter.INCREMENT_NUMBER_OF_RATINGS})

    return UserReturnPrompts.update_prompt


@HUMMUS_ROUTES.get("/hummusiot/")
async def get_hummusia_by_filter(db_filter: filter_model.DatabaseFilter):
    """
    Get all the hummusiot which stand in the criteria of the db_filter.

    :param db_filter: A filter for mongodb in dict format which the user need
    to specify in the request param

    Example:
    {
        "name": "certain name",
        "city": "regular city",
        "is_kosher": "true",
    }

    Returns an array of all the hummusiot objects (humusia_model.HumusiaModel) which
    stands in the criteria of the filter.
    """
    return DB_MANAGER._db_query.execute_query(db_filter.mongo_database_filter, DB_MANAGER.humusiot_collection)
