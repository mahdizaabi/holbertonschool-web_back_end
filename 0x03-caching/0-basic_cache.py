#!/usr/bin/python3
""" 0-basic_cache.py """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """[A basic caching system class]

    Args:
        BaseCaching ([class]): [Base Cache classs]
    """

    def __init__(self):
        super().__init__()

    def put(self, key, value):
        """[insert data to the cache]

        Args:
            key ([string]): [description]
            value ([type]): [description]
        """

        if key is None or value is None:
            return
        self.cache_data[key] = value

    def get(self, key):
        """[summary]

        Args:
            key ([string]): [description]

        Returns:
            [None or value]: [description]
        """

        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
