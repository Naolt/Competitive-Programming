# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
        
        if not cycleFound:
            return None
        else:
            #phase 2, let them meet again by slowing down the fast pointer
            slow = dummy
            while fast and slow:
                slow = slow.next
                fast = fast.next
                if fast == slow:
                    return slow