#!/usr/bin/env python3
"""[summary]
"""
import pprint
from pymongo import MongoClient


def list_all(mongo_collection):
    """[summary]
    """

    if mongo_collection.count() == 0:
        return []
    return mongo_collection.find()
