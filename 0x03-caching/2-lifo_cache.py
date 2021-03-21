#!/usr/bin/python3
""" 2-lifo_cache.py """


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Caching system Algorithm """
    lastInsertedItem = ""

    def __init__(self):
        """ constructor """
        super().__init__()

    def put(self, key, item):
        """ insert new item """
        if key is None or item is None:
            return
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            if key not in self.cache_data.keys():
                print("DISCARD: {}".format(self.__class__.lastInsertedItem))
                self.cache_data.pop(self.__class__.lastInsertedItem)

        self.cache_data[key] = item
        self.__class__.lastInsertedItem = key

    def get(self, key):
        """ eeturn the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
