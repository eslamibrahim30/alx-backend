#!/usr/bin/python3
"""
This module for task 'Basic dictionary'
"""

import base_caching


class BasicCache(base_caching.BaseCaching):
    """
    This class is used to create an instance of a basic cache.
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        This method adds an item to the cache.
        """
        if key is None or item is None:
            return None
        self.cache_data.update({key: item})

    def get(self, key):
        """
        This method gets an item from the cache.
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
