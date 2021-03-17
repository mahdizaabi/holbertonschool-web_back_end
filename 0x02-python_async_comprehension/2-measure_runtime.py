#!/usr/bin/env python3
""" measure runtime """
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure the run time of 4 concurrent data stream,
    with a delay of 10 seconds for each data Stream.
    data is collected using async comprehension .
    """
    t0 = time.time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)

    return time.time() - t0
