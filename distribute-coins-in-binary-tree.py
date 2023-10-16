# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dist(root):
            nonlocal result
            if not root:
                return 0

            left = dist(root.left)
            right = dist(root.right)
            
            total = (left + right + root.val-1)
            result += abs(total)
            
            return total
        
        dist(root)
        
        return result