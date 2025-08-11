#!/usr/bin/env python3
"""
This module provides a helper function for calculating
start and end indexes for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
