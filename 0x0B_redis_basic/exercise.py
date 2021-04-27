#!/usr/bin/env python3
"""
0x0B. Redis basic
0x0B. Redis basic
Web Stack programming ― Back-end
"""
import redis
import uuid
from typing import Union, Optional, Callable


class Cache():
    """[Caching base Class using redis]
    """

    @staticmethod
    def generate_id() -> str:
        """[static method to generate ID]
        """
        return str(uuid.uuid4())

    def __init__(self):
        """[Cache class constructor]
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """[Store a new key value pair and return the randomly generated key]

        Args:
            data ([str, bytes, int, float]): [description]
            returns: id of type string
        """
        id = Cache.generate_id()
        self._redis.mset({id: data})
        return id
