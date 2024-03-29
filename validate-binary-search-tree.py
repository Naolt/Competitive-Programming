# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.last = float(-inf)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left = self.isValidBST(root.left)
        if root.val <= self.last:
            result = False
            return result
        self.last = root.val
        right = self.isValidBST(root.right)

        return left and right