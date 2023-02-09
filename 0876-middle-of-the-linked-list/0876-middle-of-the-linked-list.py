# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        slow = dummy
        fast = dummy
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if not fast:
            return slow
        else:
            return slow.next
            