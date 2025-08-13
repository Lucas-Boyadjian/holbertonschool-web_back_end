#!/usr/bin/env python3
"""
Module that defines a function to list all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    Lists all documents in the given MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of all documents in the collection.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
