# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         dummy = ListNode(0,head)
#         slow = dummy 
#         fast = dummy
#         i = 0
#         size = 0
        
#         while(fast and fast.next):
#             i += 1
#             slow = slow.next
#             fast = fast.next.next
     
#         size = i*2
#         if not fast:
#             size -= 1
            
#         if size <= 1:
#             return None
#         elif size == 2:
#             if n == 1:
#                 head.next = None
#             else:
#                 print("here")
#                 dummy.next = dummy.next.next
#             return dummy.next
        
#         for j in range(i,size-n):
#             slow = slow.next
            
     
#         print("here",i,size,slow)
#         slow.next = slow.next.next
        size = 0
        
        dummy = ListNode(0,head)
        node = dummy.next
        while(node):
            node = node.next
            size += 1
        if size == 1:
            return None
        if size-n-1 < 0:
            dummy.next = dummy.next.next
            return dummy.next
        node = dummy.next
        i = 0
        while i < size-n-1:
            node = node.next
            i += 1
        print(node)
        if node.next:
            node.next = node.next.next
        else:
            node.next = None
        return dummy.next