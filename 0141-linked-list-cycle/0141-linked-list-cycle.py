# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(0,head)
        slow = dummy
        fast = dummy
        cycleFound = False
        # phase 1, let them meet once
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycleFound = True
                break
        return cycleFound
        
        