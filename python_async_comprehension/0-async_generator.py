#!/usr/bin/env python3
"""
This module provides an async generator that yields random
float numbers between 0 and 10.
"""

import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    Asynchronously yields 10 random float numbers
    between 0 and 10, one per second.
    Yields:
        float: a random float between 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
