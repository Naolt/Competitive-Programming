# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        def createBST(left,right):
            if not (0 <= left <= right < len(nums)):
                return None
            mid = left + (right-left)//2
            node = TreeNode(nums[mid],createBST(left,mid-1),createBST(mid+1,right))

            return node

        root = createBST(0,len(nums)-1)

        return root

        