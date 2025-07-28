#!/usr/bin/env python3
"""
This module provides an async function to run multiple wait_random
coroutines concurrently and return their delays in order of completion.
"""
import importlib
from typing import List
import asyncio

wait_random = importlib.import_module('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Launch wait_random n times with max_delay and return
    delays in order of completion.
    Args:
        n (int): number of coroutines to launch
        max_delay (int): maximum delay for wait_random
    Returns:
        List[float]: list of delays in order of completion
    """
    listDelays = []
    tasks = []
    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    for task in asyncio.as_completed(tasks):
        listDelays.append(await task)
    return listDelays
