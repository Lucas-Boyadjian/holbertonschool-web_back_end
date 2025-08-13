#!/usr/bin/env python3
"""
Module that defines a function to update the
topics of a school document in a MongoDB collection.
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics field of a school document based on the school's name.

    Args:
        mongo_collection: The pymongo collection object.
        name (str): The name of the school to update.
        topics (list): The list of topics to set for the school.

    Returns:
        The result of the update operation.
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
