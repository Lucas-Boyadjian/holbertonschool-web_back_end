#!/usr/bin/env python3
"""
This module provides an async function to collect
random numbers from an async generator using async comprehension.
"""
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """
    Collects 10 random numbers from async_generator using async comprehension.
    Returns:
        list: a list of 10 random float numbers
    """
    random_numbers = [i async for i in async_generator()]
    return random_numbers
