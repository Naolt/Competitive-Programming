from sortedcontainers import SortedSet

class TimeMap:

    def __init__(self):
        self.dic = defaultdict(SortedSet)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].add((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        index = bisect_right(self.dic[key],(timestamp,chr(126)))
        if key not in self.dic or index == 0:
            return ""
        # print(key,self.dic[key],timestamp,index)
        return self.dic[key][index-1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)