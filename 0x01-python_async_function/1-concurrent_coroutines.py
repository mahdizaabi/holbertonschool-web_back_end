#!/usr/bin/env python3
""" asynchronous coroutine """

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    delay_List = []
    for i in range(n):
        c = await wait_random(max_delay)
        delay_List.append(c)
    return delay_List
