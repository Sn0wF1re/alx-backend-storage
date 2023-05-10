#!/usr/bin/env python3
"""
Create Cache class
"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
     count how many times methods of the Cache class are called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper function
        Args:
            self:
            args: variable number of arguments
            kwargs: variable no. of keyword arguments
        Returns: decorated function
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    define a call_history decorator
    to store the history of inputs and outputs for a particular function
    """
    key = method.__qualname__
    inputs = key + ':inputs'
    outputs = key + ':outputs'

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper function
        """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data
    return wrapper


def replay(method: Callable) -> None:
    """ display the history of calls of a particular function"""
    key = method.__qualname__
    inputs = key + ':inputs'
    outputs = key + ':outputs'
    r = method.__self__.redis
    calls = r.get(key).decode('utf-8')
    print(f"{key} was called {calls} times")
    inpList = r.lrange(inputs, 0, -1)
    outList = r.lrange(outputs, 0, -1)
    for k, v in zip(inpList, outList):
        field = k.decode('utf-8')
        value = v.decode('utf-8')
        print(f"{key}(*({field})) -> {value}")


class Cache:
    """
    Define the Cache class
    """
    def __init__(self):
        """
        initializes the class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Args:
            data: input data
        Returns: randomly generated key
        """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Takes key str argument and optional callable
        to convert data back to desired format
        """
        data = self._redis.get(key)
        if fn is not None:
            data = fn(data)
        return data

    def get_str(self, data: str) -> str:
        """parameterize Cache.get to string"""
        return data.decode('utf-8')

    def get_int(self, data: int) -> int:
        """parameterize Cache.get to int"""
        return int(data)
