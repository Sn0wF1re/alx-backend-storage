#!/usr/bin/env python3
"""
Create Cache class
"""
import redis
from uuid import uuid4
from typing import Union


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
