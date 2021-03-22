#!/usr/bin/python3
""" 2-lifo_cache.py """


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache (BaseCaching):
    """LRUCache class """
    Queue = []

    def __init__(self):
        """ Constructor"""
        super().__init__()

    def reloadQueue(self, keyToRemove, keyToAppend):
        """ update and reload the Queue"""
        self.__class__.Queue.remove(keyToRemove)
        self.__class__.Queue.append(keyToAppend)

    def put(self, key, item):
        """ Assign a new value """
        if key is None or item is None:
            return None

        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.reloadQueue(key, key)
            else:
                print("DISCARD: {}".format(self.__class__.Queue[0]))
                keyToDelete = self.__class__.Queue[0]
                del self.cache_data[keyToDelete]
                self.cache_data[key] = item
                self.reloadQueue(keyToDelete, key)

        else:

            self.cache_data[key] = item
            self.__class__.Queue.append(key)

    def get(self, key):
        """get an element """
        if key is None or key not in self.cache_data.keys():
            return None
        if key not in self.__class__.Queue:
            return
        self.reloadQueue(key, key)
        return self.cache_data[key]
