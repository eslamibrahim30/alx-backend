#!/usr/bin/env python3
"""
This module for task "Hypermedia pagination"
"""
import csv
import math
from typing import (List, Tuple, Dict)


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        This method returns a dictionary containing a dictionary containing
        the following key-value pairs:
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """
        data_dict = dict()
        total_pages = 0
        data_dict['page_size'] = page_size
        data_dict['page'] = page
        data_dict['data'] = self.get_page(page, page_size)
        if len(self.__dataset) % page_size == 0:
            total_pages = len(self.__dataset) // page_size
        else:
            total_pages = len(self.__dataset) // page_size + 1
        if page >= total_pages:
            data_dict['next_page'] = None
        else:
            data_dict['next_page'] = page + 1
        if page <= 1:
            data_dict['prev_page'] = None
        else:
            data_dict['prev_page'] = page - 1
        data_dict['total_pages'] = total_pages
        return data_dict
