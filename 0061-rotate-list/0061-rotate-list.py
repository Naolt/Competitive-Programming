# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        node = head
        tail = None
        
       
        
        while node:
            size += 1
            tail = node
            node = node.next
        print(size)
        
        if size < 2:
            return head  
        
        if k > size:
            k = k%size
        
        if k == size or k == 0:
            return head
      
        node = head
        # now go until size - k
        for i in range(size-k-1):
            node = node.next
        
        remaining = node.next
        node.next = None
        tail.next = head
        
        return remaining
            
        
            