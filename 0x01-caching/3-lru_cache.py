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
        self.recent = []

    def put(self, key, item):
        """
        This method adds an item to the cache.
        """
        if key is None or item is None:
            return None
        if key in self.cache_data.keys():
            self.recent.pop(self.recent.index(key))
        elif len(self.cache_data) == self.MAX_ITEMS:
            disKey = self.recent.pop(0)
            self.cache_data.pop(disKey)
            print(f"DISCARD: {disKey}")
        self.cache_data.update({key: item})
        self.recent.append(key)

    def get(self, key):
        """
        This method gets an item from the cache.
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        self.recent.pop(self.recent.index(key))
        self.recent.append(key)
        return self.cache_data.get(key)
