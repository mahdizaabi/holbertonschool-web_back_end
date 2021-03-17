#!/usr/bin/env python3
"""async_comprehension"""


import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """[summary]

    Returns:
        [type]: [description]

    Yields:
        Generator[int, None, None]: [description]
    """
    return [x async for x in async_generator()]
