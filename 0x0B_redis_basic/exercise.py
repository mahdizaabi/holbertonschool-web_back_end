#!/usr/bin/env python3
"""
0x0B. Redis basic
0x0B. Redis basic
Web Stack programming ― Back-end
"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """[summary]

    Args:
        method (Callable): [description]

    Returns:
        Callable: [description]
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper to decorate methods """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """[summary]

    Args:
        method (Callable): [description]

    Returns:
        Callable: [description]
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper to decorate methods """
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return wrapper


def replay(fn: Callable):
    """ implement a replay function to display the history of
    calls of a particular function"""
    r = redis.Redis()
    fcName = fn.__qualname__
    calls = r.get(fcName)
    try:
        calls = calls.decode('utf-8')
    except Exception as e:
        calls = 0
    print("{} was called {} times:".format(fcName, calls))

    inputs = r.lrange(fcName + ":inputs", 0, -1)
    outputs = r.lrange(fcName + ":outputs", 0, -1)

    for inn, out in zip(inputs, outputs):
        try:
            inn = inn.decode('utf-8')
        except Exception as e:
            inn = ""
        try:
            out = out.decode('utf-8')
        except Exception as e:
            out = ""
    print("{}(*{}) -> {}".format(fcName, inn, out))


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

    @call_history
    @count_calls
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
