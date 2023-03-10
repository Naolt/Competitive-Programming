# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        middle = self.getMiddle(head)
        if middle  == head or not middle:
            return head
        left = self.sortList(head)
        right = self.sortList(middle)
        newHead = self.mergeLists(left,right)
        return newHead


    def getMiddle(self,head):
        slow,fast = head,head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if not fast:
            temp = prev.next
            prev.next = None
            return temp
        if not fast.next:
            temp = slow.next
            slow.next = None
            return temp

    def mergeLists(self,list1,list2):
        dummy = ListNode() 
        tail = dummy

        pt1 = list1
        pt2 = list2

        while pt1 and pt2:
            if pt1.val > pt2.val:
                tail.next = pt2
                pt2 = pt2.next
            else:
                tail.next = pt1
                pt1 = pt1.next
            tail = tail.next
        if pt1:
            tail.next = pt1
        if pt2:
            tail.next = pt2
        return dummy.next