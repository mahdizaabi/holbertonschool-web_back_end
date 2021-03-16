#!/usr/bin/env python3
"""The basic of async
"""

import random
import time
import asyncio


async def wait_random(max_delay=10):
    """[summary]

    Args:
        max_delay (int, optional): [description]. Defaults to 10.

    Returns:
        [type]: [description]
    """
    secure_random = random.SystemRandom()

    delay = secure_random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
