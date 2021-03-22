#!/usr/bin/python3
""" 100-lfu_cache.py """


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """MRUCache class """
    Queue = []
    mostUsed = {}

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
                if key in self.__class__.Queue:
                    self.__class__.Queue.remove(key)
                if key in self.__class__.mostUsed:
                    usageFrequency = self.__class__.mostUsed[key]
                    self.__class__.mostUsed.pop(key, None)
                    self.__class__.mostUsed[key] = usageFrequency + 1
                else:
                    self.__class__.mostUsed[key] = 2

            else:
                if len(self.__class__.Queue) != 0:
                    print("DISCARD: {}".format(
                        self.__class__.Queue[0]))
                    keyToDelete = self.__class__.Queue[0]
                    del self.cache_data[keyToDelete]
                    self.cache_data[key] = item
                    self.reloadQueue(keyToDelete, key)
                else:
                    keyx = sorted(self.__class__.mostUsed,
                                  key=self.__class__.mostUsed.get)[0]
                    print("DISCARD: {}".format(keyx))
                    del self.cache_data[keyx]
                    self.__class__.mostUsed.pop(keyx, None)
                    self.cache_data[key] = item
                    self.__class__.Queue.append(key)

        else:

            self.cache_data[key] = item
            self.__class__.Queue.append(key)

    def get(self, key):
        """Request an item from the cache """
        if key is None or key not in self.cache_data.keys():
            return None
        # if key not in self.__class__.Queue:
            # return
        if key not in self.__class__.mostUsed:
            self.__class__.mostUsed[key] = 2
            self.__class__.Queue.remove(key)

        else:
            self.__class__.mostUsed[key] = self.__class__.mostUsed[key] + 1

        return self.cache_data[key]
