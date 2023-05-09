#!/usr/bin/env python3
"""
create function schools_by_topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic
    Args:
        mongo_collection: pymongo collection
        topic: (string) topic to be searched
    Returns: List of school having a specific topic
    """
    return mongo_collection.find( {"topics": topic} )
