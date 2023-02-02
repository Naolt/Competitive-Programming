# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        newDummy = ListNode()
        newTail = newDummy
        
        tail = dummy 
        while tail and tail.next:
            node = tail
            while node and node.next and node.next.val >= x:
                newTail.next = node.next
                newTail = node.next
                node = node.next
            tail.next = node.next
            if node.next:
                tail = node.next
        print(dummy,newDummy,tail,newTail)
        newTail.next = None
        tail.next = newDummy.next
        return dummy.next
        
            
            
                