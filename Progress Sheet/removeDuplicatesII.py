# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        parent = ListNode(0,None)
        if head == None or head.next == None:
            return head
        
        node = head
        head = parent
        
        while node != None and node.next != None:
            if(node.next != None and node.next.val == node.val):
                while( node.next != None and node.next.val == node.val ):
                    node = node.next
                parent.next = node.next
            else:
                parent.next = node
                parent = parent.next
            node = node.next

        return head.next
            
