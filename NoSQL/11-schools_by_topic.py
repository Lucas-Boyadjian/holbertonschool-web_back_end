#!/usr/bin/env python3
"""
Module that defines a function to find all school documents with a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Finds all school documents where the topics field contains the given topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        A list of school documents matching the topic.
    """
    return list(mongo_collection.find({"topics": topic}))
