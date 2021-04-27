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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """[Get value from redis storage and decode it]
        """

        if fn is None:
            return self._redis.get(key)
        encodedValue = self._redis.get(key)
        if encodedValue is None:
            return None

        return fn(encodedValue)

    def get_str(self, value: bytes) -> str:
        """[summary]

        Args:
            value ([type]): [description]
        """

        return value.decode("utf-8")

    def get_int(self, value: bytes) -> str:
        """[summary]

        Args:
            value ([type]): [description]
        """

        return int(value.decode("utf-8"))
