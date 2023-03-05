class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        # self.count = 0
        self.queue = []
        self.k = k
        

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.queue.append(num)
        else:
            self.queue.clear()
        return len(self.queue) >= self.k 
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)