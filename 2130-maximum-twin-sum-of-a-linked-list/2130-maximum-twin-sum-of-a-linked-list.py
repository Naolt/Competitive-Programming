# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # reverse the linked list upto the middle
        prev,curr = None,head
        fast = ListNode(0,head)
        result = 0
        while fast.next:
            fast = fast.next.next
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # sum and iterate
        while prev:
            result = max(result,prev.val+curr.val)
            prev = prev.next
            curr = curr.next
            
        return result
            
            