#!usr/bin/python3
"""2-lifo_cache.py"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """Fifo Cache class"""
    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Add an item in the cache.
        If the number of items in,
        remove the last  (LIFO).
        If key or item is None, .
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.stack.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.stack.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        """
        Get an item by key.
        If key is None  return None.
        """
        return self.cache_data.get(key, None)
