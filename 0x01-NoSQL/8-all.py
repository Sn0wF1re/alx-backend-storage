#!/usr/bin/env python3
"""
Create a list_all function
"""
import pymongo


def list_all(mongo_collection):
    """
    lists all documents in a collection
    Args:
        mongo_collection: pymongo collection object
    Returns: List of documents in a collection
            If no documents, empty list
    """
    return mongo_collection.find()
