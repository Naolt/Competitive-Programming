# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        nums = []
        dummy = ListNode()
        tail = dummy
        for head in lists:
            while head:
                nums.append(head.val)
                head = head.next
        nums.sort()
        for num in nums:
            node = ListNode(num,None)
            tail.next = node
            tail = tail.next
        return dummy.next