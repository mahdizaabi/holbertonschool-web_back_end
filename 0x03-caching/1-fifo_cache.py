#!/usr/bin/python3
""" 1. FIFO caching """


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class"""

    def __init__(self):
        """ Class constructor"""
        super().__init__()

    def put(self, key, item):
        """ assign to the dictionary self.cache_data
        the item value for the key key."""

        if key not in self.cache_data.keys():
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                keyToRemove = sorted(self.cache_data)[0]
                print("DISCARD: {}".format(keyToRemove))
                self.cache_data.pop(keyToRemove)
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key """
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
