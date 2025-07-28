#!/usr/bin/env python3
"""
This module provides an asynchronous function to wait for a random delay.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay between 0 and max_delay seconds.
    Args:
        max_delay (int): maximum number of seconds to wait
    Returns:
        float: the actual delay waited
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
