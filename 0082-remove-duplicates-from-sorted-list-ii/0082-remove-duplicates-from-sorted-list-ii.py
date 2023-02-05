# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(-200,head)
        tail = dummy
        prev = tail.next
        curr = prev.next
        while prev and curr:
            while curr and curr.val == prev.val:
                
                curr = curr.next
            if prev and curr and prev.next.val == curr.val:
                
                tail.next = prev
                tail = tail.next
                prev = curr
                curr = curr.next
            else:
                
                prev = curr
                if not curr or not curr.next:
                    tail.next = curr
                    break
                if curr:
                    curr = curr.next
            
            
        return dummy.next