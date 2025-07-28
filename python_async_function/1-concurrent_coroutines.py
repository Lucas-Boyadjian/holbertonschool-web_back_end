#!/usr/bin/env python3

import importlib
from typing import List
import asyncio

wait_random = importlib.import_module('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Launch wait_random n times with max_delay and return delays in order of completion.
    """
    listDelays = []
    tasks = []
    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    for task in asyncio.as_completed(tasks):
        listDelays.append(await task)
    return listDelays
