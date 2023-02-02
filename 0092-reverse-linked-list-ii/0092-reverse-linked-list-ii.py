# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        prevStart = None
        start = None
        end = None
        nextEnd = None
        
        #search for the left
        i = 0
        leftNode = ListNode(-600,head)
        while(leftNode):
            if i == left-1:
                break
            leftNode = leftNode.next
            i += 1
            
        start = leftNode.next
        #reverse the node until I reach the right node
        
        if leftNode.val < -500 and not leftNode.next.next:
            
            return leftNode.next
        else:
            prev = leftNode.next
            curr = leftNode.next.next
        
    
        while(curr):
            
            if i == right-1:
                break
                
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            
            i += 1
        
        #then reconnect the start and end
        leftNode.next = prev
        start.next = curr
        
        if leftNode.val < -500:
            return leftNode.next
        
        return head
        
                
        
        