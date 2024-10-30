#!/usr/bin/env python3
""" Basic dictionary """


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ a caching system """
    def __init__(self):
        """Initilize"""
        super().__init__()

    def put(self, key, item):
        """ assign to a cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ return value from cache """
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data[key]
