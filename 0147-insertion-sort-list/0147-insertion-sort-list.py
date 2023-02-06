# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-6000,head)
        parent = dummy
        prev = head
        curr = head.next
        
        while curr:
            
            if curr.val < prev.val:
                head = dummy
                while head.next and head.next.val < curr.val:
                    head = head.next
                
                #position found so assign
                prev.next = prev.next.next
                temp = head.next
                head.next = curr
                # temp.next = curr.next
                curr.next = temp
                
                # print(prev,'        ',curr) 
                curr = prev.next
            else:
                prev = prev.next    
                curr = prev.next
                

            # print(dummy.next,prev.val,curr.val)
        return dummy.next