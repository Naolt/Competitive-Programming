# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkBalanced(root)[0]

    def checkBalanced(self,root):
        if not root:
            return [True,0]        
        leftDepth = self.checkBalanced(root.left)
        rightDepth = self.checkBalanced(root.right)
        if not (leftDepth[0] and rightDepth[0]):
            return [False,0] 
        if abs(leftDepth[1]-rightDepth[1]) < 2:
            return [True,max(leftDepth[1],rightDepth[1])+1]
        else:
            return [False,0]