#!/usr/bin/env python3
""" Impleminting FIFO Algorithm"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO Algorithm"""
    def __init__(self):
        """
        Initilization
        """
        super().__init__()
        self.keep_track = []

    def put(self, key, item):
        """
        put value to cache using fifo method
        """
        if key is not None and item is not None:
            if len(self.cache_data) <= BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
                self.keep_track.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.keep_track[0]))
                self.cache_data.pop(self.keep_track[0])
                self.keep_track.pop(0)

    def get(self, key):
        """
        return a value from the cache
        """
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data[key]
