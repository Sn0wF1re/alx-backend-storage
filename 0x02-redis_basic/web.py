#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""
import requests
import redis

r = redis.Redis()
count = 0


def get_page(url: str) -> str:
    """
    uses the requests module to obtain the HTML content
    of a particular URL and returns it
    Args:
        url: url to be queried
    Returns: HTML content
    """
    cached = 'cached:' + url
    r.set(cached, count)
    response = requests.get(url)
    countKey = 'count:' + url
    r.incr(countKey)
    val = r.get(cached)
    r.set(cached, val, ex=10)
    return response.text


if __name__ == "__main__":
    get_page("http://slowwly.robertomurray.co.uk")
