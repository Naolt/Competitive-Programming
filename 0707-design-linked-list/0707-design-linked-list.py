class Node:
    
    def __init__(self,val,next):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def getNode(self,index: int)-> Node:
        node = self.head
        for i in range(index):
            node = node.next
        return node
        

    def get(self, index: int) -> int:
        
        if index < 0 or index >= self.size:
            return -1
        
        return (self.getNode(index)).val
            
    def addAtHead(self, val: int) -> None:
        newNode = Node(val,self.head)
        if self.size == 0:
            self.head = self.tail = newNode
        else:
            self.head = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newNode = Node(val,None)
        if self.size == 0:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
     
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            nodeBefore = self.getNode(index-1)
            newNode = Node(val,nodeBefore.next)
            nodeBefore.next = newNode
            self.size += 1
            
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            if self.size == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next
        else:
            beforeNode = self.getNode(index-1)
            if index == self.size-1:
                beforeNode.next = None
                self.tail = beforeNode
            else:
                beforeNode.next = beforeNode.next.next
        self.size -= 1
            
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)