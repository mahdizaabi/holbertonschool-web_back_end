#!/usr/bin/python3
""" 4-mru_cache.py """


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache (BaseCaching):
    """MRUCache class """
    Queue = []

    def __init__(self):
        """ Constructor"""
        super().__init__()

    def reloadQueue(self, keyToRemove, keyToAppend):
        """ update and reload the Queue"""
        self.__class__.Queue.remove(keyToRemove)
        self.__class__.Queue.append(keyToAppend)

    def put(self, key, item):
        """ place an item in the cache """
        if key is None or item is None:
            return None

        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.reloadQueue(key, key)
            else:
                print("DISCARD: {}".format(self.__class__.Queue[len(
                    self.__class__.Queue) - 1]))

                keyToDelete = self.__class__.Queue[len(
                    self.__class__.Queue) - 1]
                del self.cache_data[keyToDelete]
                self.cache_data[key] = item
                self.reloadQueue(keyToDelete, key)

        else:

            self.cache_data[key] = item
            self.__class__.Queue.append(key)

    def get(self, key):
        """Request an item from the cache """
        if key is None or key not in self.cache_data.keys():
            return None
        if key not in self.__class__.Queue:
            return
        self.reloadQueue(key, key)
        return self.cache_data[key]
