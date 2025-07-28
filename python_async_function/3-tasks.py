#!/usr/bin/env python3
"""
This module provides a function to create and return
an asyncio.Task for the wait_random coroutine.
"""
import importlib
import asyncio

wait_random = importlib.import_module('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task for wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))
