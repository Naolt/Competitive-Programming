# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy
        
        k = len(lists)
        
        
        while(lists):
            allVisited = []
            for i in range(k):
                if not lists[i]:
                    allVisited.append(i)
            for i,value in enumerate(allVisited):
                lists.pop(value-i)
            
            index = 0
            k = len(lists)
            if k == 0:
                return dummy.next
            
            for i in range(k):
                if lists[i].val < lists[index].val:
                    index = i
            tail.next = lists[index]
            tail = tail.next
            lists[index] = lists[index].next
            
            
            
      