# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root or (not root.left and not root.right):
            return 0
        
        total = 0
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val
        else:
            total += self.sumOfLeftLeaves(root.left)
        
        total += self.sumOfLeftLeaves(root.right)

        return total