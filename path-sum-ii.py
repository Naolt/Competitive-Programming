# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def getPathSum(node,path):
            if not node:
                return []
            path.append(node.val)
            if not node.left and not node.right:
                if sum(path) == targetSum:
                    return [path]
                else:
                    return []
            
            left,right = [],[]
            if node.left:
                left = getPathSum(node.left,path[:])
            if node.right:
                right = getPathSum(node.right,path[:])

            return left+right
        
        return getPathSum(root,[])