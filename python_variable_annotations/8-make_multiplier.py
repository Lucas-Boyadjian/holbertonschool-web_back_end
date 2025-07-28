#!/usr/bin/env python3
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.
    Args:
        multiplier (float): the multiplier value
    Returns:
        Callable[[float], float]: a function that multiplies
        its argument by multiplier
    """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
