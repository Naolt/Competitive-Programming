# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0,head)
        prev = head
        head = head.next
        
        while head:
            while prev and head and prev.val == head.val :
                head = head.next
            prev.next = head
            prev = prev.next
            if prev:
                head = prev.next
            else:
                head = None
        return dummy.next
            
                
            
    