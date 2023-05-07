# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        result = str(root.val)

        left = self.tree2str(root.left)
        right = self.tree2str(root.right)

        if left == "" and right == "":
            return result
        if left or right:
            result += ("(" + left + ")")
        if right:
            result += ("(" + right + ")")
        return result