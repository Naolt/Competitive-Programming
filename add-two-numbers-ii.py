# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1,num2 = "",""

        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        
        sum_ = int(num1) + int(num2)

        result = list(map(lambda x:ListNode(int(x)), list(str(sum_))))
        for i in range(len(result)-1):
            result[i].next = result[i+1]

        return result[0]