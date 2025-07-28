#!/usr/bin/env python3
from typing import List
from typing import Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing integers and floats.
    Args:
        mxd_lst (List[Union[int, float]]): list of integers and floats
    Returns:
        float: the sum of all elements in the list
    """
    return sum(mxd_lst)
