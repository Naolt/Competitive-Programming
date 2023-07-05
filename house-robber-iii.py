# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = defaultdict(int)

        def dp(current):

            if not current:
                return 0

            if current not in memo:
                
                currentNotRobbed = dp(current.left) + dp(current.right)
                currentRobbed = current.val
                
                if current.left:
                    currentRobbed += dp(current.left.left) + dp(current.left.right)
                if current.right:
                    currentRobbed += dp(current.right.left) + dp(current.right.right)
                
                memo[current] = max(currentNotRobbed,currentRobbed)

            return memo[current]

        return dp(root)