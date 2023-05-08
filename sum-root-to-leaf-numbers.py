# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
       return int(self.addDown(root,""))

    def addDown(self,root,currentSum):
        currentSum += str(root.val)
        left,right = "",""
        if not root.left and not root.right:
            return currentSum
        if root.left:
            left = self.addDown(root.left,currentSum)
        if root.right:
            right = self.addDown(root.right,currentSum)
        total = 0
        if left:
            total += int(left)
        if right:
            total += int(right)
        return total