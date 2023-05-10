#!/usr/bin/env python3
"""
Create Cache class
"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable


class Cache:
    def __init__(self):
        """
        initializes the class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

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
