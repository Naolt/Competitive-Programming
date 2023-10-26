# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = None

        def traverse(root,i):
            nonlocal result
            if not root:
                return i
            
            left = traverse(root.left,i)
            if left + 1 == k:
                result = root.val
            right = traverse(root.right,left+1)
            
            return right

        traverse(root,0)
        return result