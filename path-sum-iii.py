# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        numDict = defaultdict(int)
        numDict[0] = 1

        def getPathSum(node,total):
            if not node:
                return 0
            total += node.val 
            result = 0
            if total - targetSum in numDict:
                result += numDict[total-targetSum]
            numDict[total] += 1
            result += getPathSum(node.left,total) 
            result += getPathSum(node.right,total)
            numDict[total] -= 1

            if numDict[total] == 0:
                del numDict[total]

            return result 
           

        return getPathSum(root,0)