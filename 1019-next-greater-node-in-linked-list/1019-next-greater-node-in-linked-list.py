# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
#         DISCUSS OPTIMAL SOLUTION
        values = []
        
        while head:
            values.append(head.val)
            head = head.next
        
        stack = []
        answer = [0]*len(values)
        
        for i ,value in enumerate(values):
            while stack and values[stack[-1]] < value:
                answer[stack.pop()] = value
            stack.append(i)
            
        return answer
        
        
#         stack,answer = [],[]
        
#         prev = None
#         curr = head
#         #reversed
#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp
#         head = prev
#         dummy = ListNode(0,head)
        
#         while head:
#             #if stack is empty there is no element so put zero
#             if not stack:
#                 answer.append(0)
#                 stack.append(head.val)
#                 head = head.next
#             else:
#                 if stack[-1] > head.val:
#                     answer.append(stack[-1])
#                     stack.append(head.val)
#                     head = head.next
#                 else:
#                     stack.pop()
                    
#         return answer[::-1]
            
            
#TIME LIMIT EXCEEDED
#         curr = head
#         greater = head
        
#         answer = []
        
#         while curr:
            
#             while greater and greater.val <= curr.val:
#                 greater = greater.next
#             answer.append(greater.val if greater else 0)
#             curr = curr.next
#             greater = curr
            
#         return answer

# TRYING OPTIMAL SOLN FROM DISCUSS
        

        


