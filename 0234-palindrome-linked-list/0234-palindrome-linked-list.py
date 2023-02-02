# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        left = head
        right = head
        dummy = ListNode(0,head)
        slow,fast = head,head
        prev = None
        curr = head
        while(left and right):
            
            
            # if it is even
            if not fast:
                left = prev
                right = curr
                
                while left and right and left.val == right.val:
                    left = left.next
                    right = right.next
                if not left and not right:
                    return True
                else:
                    return False
                
            # if it is odd
            elif not fast.next:
                left = prev
                right = curr.next
                
                while left and right and left.val == right.val:
                    left = left.next
                    right = right.next
                if not left and not right:
                    return True
                else:
                    return False
                
            slow = slow.next
            fast = fast.next.next
            
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
                
                
        