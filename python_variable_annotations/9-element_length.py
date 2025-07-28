#!/usr/bin/env python3
from typing import List, Iterable, Sequence, Tuple, Union


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each sequence and its length.
    """
    return [(i, len(i)) for i in lst]
