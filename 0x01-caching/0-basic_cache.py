#!usr/bin/python3
"""0-basic-caching"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    Creation of Basic Cache 
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item to  cache."""
        if key is None or item is None:
            return
        self.cache_data[str(key)] = item

    def get(self, key):
        """Retrieve an item from  cache."""
        if key is None and key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
