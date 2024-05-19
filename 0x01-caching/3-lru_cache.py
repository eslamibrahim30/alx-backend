#!/usr/bin/python3
"""
This module for task 'LRU Caching'
"""

import base_caching


class LRUCache(base_caching.BaseCaching):
    """
    This class is used to create an instance of a LRU cache.
    """
    def __init__(self):
        super().__init__()
        self.usage = {}

    def put(self, key, item):
        """
        This method adds an item to the cache.
        """
        if key is None or item is None:
            return None
        if len(self.cache_data) == self.MAX_ITEMS:
            disKey = list(self.cache_data.keys())[0]
            usageRate = self.usage[disKey]
            for key in self.cache_data.keys():
                if self.usage[key] < usageRate:
                    disKey = key
                    usageRate = self.usage[key]
            self.cache_data.pop(disKey)
            print(f"DISCARD: {disKey}")
        self.usage.update({key: 0})
        self.cache_data.update({key: item})

    def get(self, key):
        """
        This method gets an item from the cache.
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        self.usage[key] += 1
        return self.cache_data.get(key)
