#!/usr/bin/env python3
"""
Implement an expiring web cache and tracker
0x0B. Redis basic
Web Stack programming ― Back-end
"""
import redis
import requests
from typing import Union, Optional, Callable
from functools import wraps

r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """ * calculate nombre of request made by the server
        * cache the response on the redis instance
        * return the html from the cache if chache has not expired
    """

    @wraps(method)
    def wrapper(url):
        """ Wrapper for the decorated function """

        # check if the cache has a copy of the page if yes,
        # return the page from cache, otherwise make a new request
        cached_html = r.get("cached_html:{}".format(url))
        if cached_html:
            return cached_html.decode('utf-8')

        # track nombre of request made by the server to load html
        r.incr("count:{}".format(url))

        # make a new request
        html = method(url)
        # make  a new copy on the chache with 10 sec of expiration
        r.setex("cached_html:{}".format(url), 10, html)

        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """track how many time the server has sent a request
    """
    req = requests.get(url)
    return req.text
