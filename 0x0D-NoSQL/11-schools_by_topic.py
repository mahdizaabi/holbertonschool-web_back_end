#!/usr/bin/env python3
"""[summary]
"""
import pprint
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """[function that returns the list of school having an array containing a specific topic]

    Args:
        mongo_collection ([collection object]): [collection]
        topic ([string]): [string]
    """


    return mongo_collection.find( { "topics": { "$all": [topic] } } )