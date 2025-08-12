#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary with pagination information
        resilient to deletions.
        - index: The current start index of the page
        - next_index: The start index for the next page
        - page_size: Number of items per page
        - data: List of rows for the current page

        Args:
            index (int): The current start index (must be valid and >= 0).
            page_size (int): The number of items per page.

        Returns:
            Dict: Pagination metadata and page data.
        """

        next_index = None
        data = []
        indexed_dataset = self.indexed_dataset()

        assert isinstance(index, int)
        assert index >= 0 and index < len(indexed_dataset)

        for i in range(index, len(indexed_dataset)):
            if indexed_dataset.get(i) is not None:
                data.append(indexed_dataset[i])
                if len(data) == page_size:
                    next_index = i + 1
                    break

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
