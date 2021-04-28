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
    """[keep track of all the inputs and outputs of a function]

    Args:
        method (Callable): [function to be decorated]

    Returns:
        Callable: [the bundled 2 functions: the inner-wrapper function and
                the decorated]
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper to wrap the decorated function """
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return wrapper


def replay(fn: Callable):
    """ implement a replay function to display the history of
    calls of a particular function"""
    # generate the keys of input/output list stored on Redis
    functionName = fn.__qualname__
    inputListKey = functionName + ":inputs"
    outputListKey = functionName + ":outputs"
    # get the number of calls to the function:
    r = redis.Redis()
    number_calls = r.get(functionName).decode('utf-8')
    print("{} was called {} times:".format(functionName, number_calls))

    # get list of inpus and ouputs:
    inputs = r.lrange(inputListKey, 0, -1)
    outputs = r.lrange(outputListKey, 0, -1)
    for inp, out in zip(inputs, outputs):
        inp = inp.decode("utf-8")
        out = out.decode("utf-8")
        print("{}(*{}) -> {}".format(functionName, inp, out))


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
