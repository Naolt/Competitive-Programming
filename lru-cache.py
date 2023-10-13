class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.store = OrderedDict()
        
    def get(self, key: int) -> int:
        if key in self.store:
            val = self.store[key]
            del self.store[key]
            self.store[key] = val
            return self.store[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.store:
            if len(self.store) >= self.size:
                k,v = self.store.popitem(last=False)
        else:
            del self.store[key]
        self.store[key] = value

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)