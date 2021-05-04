#!/usr/bin/env python3
"""[summary]
"""
import pprint
from pymongo import MongoClient

def update_topics(mongo_collection, name, topics):
    """[summary]

    Args:
        mongo_collection ([collection object]): [collection inside my_db database]]
        name ([school name: filter the docs by the scchool name]): [string]
        topics ([list of topic to be inserted on the dociment]): [description]
    """
    mongo_collection.update_many({"name":name}, {"$set": {"topics":topics}})
