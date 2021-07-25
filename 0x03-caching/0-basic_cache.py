#!/usr/bin/env python3
""" caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ a basic caching system class
    """

    def put(self, key, item):
        """ function put
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ function get
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None