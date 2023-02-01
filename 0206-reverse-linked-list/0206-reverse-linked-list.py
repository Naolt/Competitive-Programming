# Definition for singly-linked list.
"""
[1,2,3,4,5]:
 1

parent 1 None
child 1 None
temp 2

while child.next:
child.next = parent
temp = 2


"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head and head.next:
            child = head #2
            parent = None #1
            while child.next:
                temp = child.next
                child.next = parent #2
                parent = child #3
                child = temp #4
                           
            child.next = parent
            head = child
        return head
            