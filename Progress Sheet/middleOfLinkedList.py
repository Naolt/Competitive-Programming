# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevIndex = 0

        if(head == None or head.next == None):
            return head
        middle  = head,
        middle = middle[0]
        current = head
        n = 0
        while(True):
            
            current = current.next
            n+=1
            if((n/2) > prevIndex):
                middle = middle.next
                prevIndex+=1
            if(current.next == None):
                break
        return middle
         
