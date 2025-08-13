#!/usr/bin/env python3
"""
Module that defines a function to insert a
new document into a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the specified MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: Key-value pairs representing the document fields.

    Returns:
        The _id of the newly inserted document.
    """
    document = mongo_collection.insert_one(kwargs)
    return document.inserted_id
