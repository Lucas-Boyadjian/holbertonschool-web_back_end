#!/usr/bin/env python3
"""
This module provides a coroutine to measure the
runtime of running async_comprehension concurrently.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of running async_comprehension
    4 times concurrently.
    Returns:
        float: the elapsed time in seconds
    """
    start_chrono = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    stop_chrono = time.perf_counter()

    return stop_chrono - start_chrono
