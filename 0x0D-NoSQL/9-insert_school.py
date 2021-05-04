#!/usr/bin/env python3
"""[summary]
"""
import pprint
from pymongo import MongoClient



def insert_school(mongo_collection, **kwargs):
    """[summary]

    Args:
        mongo_collection ([type]): [description]
    """
    document = {}

    for k, v in kwargs.items():
        document[str(k)] = v
    id = mongo_collection.insert(document)
    return id
