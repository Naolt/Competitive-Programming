# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddDummy = ListNode()
        odd = oddDummy
        evenDummy = ListNode()
        even = evenDummy
        while head and head.next:
            
            odd.next = head
            even.next = head.next
            head = head.next.next
            odd = odd.next
            even = even.next

        if head:
            odd.next = head
            odd = odd.next
        even.next = None
        odd.next = evenDummy.next
        
            
        
        return oddDummy.next
        
        