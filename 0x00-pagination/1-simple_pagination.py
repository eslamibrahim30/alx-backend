#!/usr/bin/env python3
"""
This module for task "Simple pagination"
"""
import csv
import math
from typing import (List, Tuple)


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    This function returns a tuple of size two containing a start index and
    an end index corresponding to the range of indexes to return in a list.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        This method initializes the server object.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        This method caches the dataset in the server object.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        This method returns the appropriate page of the dataset.
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        data_range = index_range(page, page_size)
        self.__dataset = self.dataset()
        if data_range[1] >= len(self.__dataset):
            return list()
        return self.__dataset[data_range[0]: data_range[1]]
