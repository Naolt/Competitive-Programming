class MyHashMap:

    def __init__(self):
        self.store = [-1]*(10**6+2)
        

    def put(self, key: int, value: int) -> None:
        self.store[key] = value


    def get(self, key: int) -> int:
        return self.store[key]
        

    def remove(self, key: int) -> None:
        self.store[key] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)