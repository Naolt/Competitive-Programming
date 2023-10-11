# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.parent = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.getCommon(root,p,q)
        return self.parent
    def getCommon(self,root,p,q):
        left = False
        right = False
        middle = False
        if not root:
            return False
        if not self.parent:
            if root.val == p.val or q.val == root.val:
                middle = True
            left = self.getCommon(root.left,p,q)
            right = self.getCommon(root.right,p,q)
            if (left and right) or (middle and left) or (middle and right):
                self.parent = root

        return left or right or middle