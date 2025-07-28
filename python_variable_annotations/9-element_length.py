#!/usr/bin/env python3

"""
This module provides a function to return the length
of each sequence in an iterable.
"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each sequence and its length.
    """
    return [(i, len(i)) for i in lst]
