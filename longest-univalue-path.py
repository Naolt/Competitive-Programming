# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxDepth = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.getValueDepth(root.right,root.val)+self.getValueDepth(root.left,root.val),self.longestUnivaluePath(root.left),self.longestUnivaluePath(root.right))
        


    def getValueDepth(self,root,value):
        if not root:
            return 0
        
        if root.val != value:
            return 0
        else:
            return max(1 + self.getValueDepth(root.left,value),1+self.getValueDepth(root.right,value))