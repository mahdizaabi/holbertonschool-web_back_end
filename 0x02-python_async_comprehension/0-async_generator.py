#!/usr/bin/env python3
""" asynchronous generator """


import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """[summary]
    async function generator 
    Yields:
        [Generator]: [iterable object of floats]
    """
    for _ in range(10):
        x = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield x
