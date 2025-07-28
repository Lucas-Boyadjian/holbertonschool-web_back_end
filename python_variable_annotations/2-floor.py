#!/usr/bin/env python3
"""
This module provides a function to return the floor of
a floating point number as an integer, with type annotations.
"""
import math


def floor(n: float) -> int:
    """
    Returns the floor of a float as an integer.
    Args:
        n (float): the number to floor
    Returns:
        int: the floored value of n

    """
    return math.floor(n)
