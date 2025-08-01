#!/usr/bin/env python3
"""
This module provides a function to measure the average runtime
of running multiple wait_n coroutines concurrently.
"""
import importlib
import asyncio
import time

wait_n = importlib.import_module('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average runtime of wait_n(n, max_delay).
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
