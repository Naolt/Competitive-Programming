class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []
        self.elems = defaultdict(int)
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or  self.minStack[-1] >= val:
            self.minStack.append(val)
        self.elems[val] += 1
        

    def pop(self) -> None:
        last = self.stack.pop()
        if self.minStack[-1] == last:
            self.minStack.pop()
        self.elems[last] -= 1
        if not self.elems[last]:
            del self.elems[last]
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        
        while self.minStack[-1] not in self.elems:
            self.minStack.pop()
        return self.minStack[-1] 
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()