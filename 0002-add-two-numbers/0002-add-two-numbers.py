# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0,l2)
        carry = 0
        
        while l1 and l2:
            
            if l1.val + l2.val+ carry > 9:
                l2.val = int(str(l1.val+l2.val+carry)[1])
                carry = 1
            else:
                l2.val = l1.val + l2.val + carry
                carry = 0
                
            if l1.next or l2.next:
                if not l1.next:
                    l1.next = ListNode(0,None)
                if not l2.next:
                    l2.next = ListNode(0,None)
            if not l1.next and not l2.next:
                if carry == 1:
                    l2.next = ListNode(1,None)
                    l2 = l2.next
                
            l1 = l1.next
            l2 = l2.next
            
        
        return dummy.next
            
                
                
        