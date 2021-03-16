#!/usr/bin/env python3
""" asynchronous coroutine """

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """[summary]

    Args:
        n (int): [description]
        max_delay (int): [description]

    Returns:
        List[float]: [description]
    """
    tasks = []
    delay = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))
    for future in asyncio.as_completed(tasks):
        returnx = await future
        delay.append(returnx)

    return delay
