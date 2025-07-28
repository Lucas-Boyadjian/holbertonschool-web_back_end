#!/usr/bin/env python3
from typing import Union
from typing import Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string and the square of the number as a float.
    """
    return k, float(v * v)
