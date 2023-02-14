# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        i = 1
        check = head
        while check and i != k:
            check = check.next
            i += 1
        
        if not check:
            return head
        else:
            prev = self.reverseKGroup(check.next,k)
            curr = head
            
            for j in range(k):
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            return prev
        