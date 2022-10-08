class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        if(x < 1 or x > 9):
            return
        self.stack1.append(x)

    def pop(self) -> int:
        
        if self.empty():
            return
        
        if self.stack1 and not self.stack2:
            while(len(self.stack1) !=0 ):
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        
        return self.stack2.pop()

    def peek(self) -> int:
         
        if self.empty():
            return
        
        if self.stack1 and not self.stack2:
            temp = 0
            while(len(self.stack1) !=0 ):
                temp = self.stack1.pop()
                self.stack2.append(temp)
            return temp
        
        temp = self.stack2.pop()
        self.stack2.append(temp)
        return temp
        

    def empty(self) -> bool:
        if self.stack1 or self.stack2:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
