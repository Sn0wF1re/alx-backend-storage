#!/usr/bin/env python3
"""
Create function insert_school
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs
    Args:
        mongo_collection: pymongo collection object
    Returns: new _id
    """
    newDoc = mongo_collection.insert_one(kwargs)
    return newDoc.inserted_id
