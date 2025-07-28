#!/usr/bin/env python3

"""
This module provides a function to return the sum
of a list of floats, with type annotations.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.
    """
    return sum(input_list)
