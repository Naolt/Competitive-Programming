class RandomizedSet:

    def __init__(self):
        self.store = []
        self.indices = defaultdict(int)
        

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        else:
            self.indices[val] = len(self.store)
            self.store.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.store:
            self.indices[self.store[-1]] = self.indices[val]
            self.store[self.indices[val]],self.store[-1] = self.store[-1],self.store[self.indices[val]]
            self.store.pop()
            del self.indices[val]
            return True
        else:
            return False 

    def getRandom(self) -> int:
        return random.choice(self.store)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()