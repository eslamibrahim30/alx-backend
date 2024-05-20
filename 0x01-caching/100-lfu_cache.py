#!/usr/bin/python3
"""
This module for task 'LFU Caching'
"""

import base_caching


class LFUCache(base_caching.BaseCaching):
    """
    This class is used to create an instance of a LFU cache.
    """
    def __init__(self):
        super().__init__()
        self.usage = {}
        self.recent = []

    def put(self, key, item):
        """
        This method adds an item to the cache.
        """
        if key is None or item is None:
            return None
        if key in self.cache_data.keys():
            self.recent.pop(self.recent.index(key))
            self.usage[key] += 1
            self.cache_data.update({key: item})
            self.recent.append(key)
        elif len(self.cache_data) == self.MAX_ITEMS:
            disKey = list(self.cache_data.keys())[0]
            disIndex = self.recent.index(disKey)
            disUsage = self.usage[disKey]
            for k in self.cache_data.keys():
                curUsage = self.usage[k]
                curIndex = self.recent.index(k)
                if curUsage < disUsage:
                    disKey = k
                    disIndex = curIndex
                    disUsage = curUsage
                elif curUsage == disUsage and curIndex < disIndex:
                    disKey = key
                    disIndex = curIndex
                    disUsage = curUsage
            self.cache_data.pop(disKey)
            self.usage.pop(disKey)
            self.recent.pop(disIndex)
            print(f"DISCARD: {disKey}")
            self.cache_data.update({key: item})
            self.usage.update({key: 0})
            self.recent.append(key)
        else:
            self.cache_data.update({key: item})
            self.usage.update({key: 0})
            self.recent.append(key)

    def get(self, key):
        """
        This method gets an item from the cache.
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        self.recent.pop(self.recent.index(key))
        self.recent.append(key)
        self.usage[key] += 1
        return self.cache_data.get(key)
