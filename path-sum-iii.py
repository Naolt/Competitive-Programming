# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        queue = deque()
        return self.getPaths(root,queue,0,targetSum)
    
    def getPaths(self,root,current,total,target):
        # print(current)
        total = sum(current)
        if not root:
            return 0
        found = 0
        current.append(root.val)
        total += root.val
        if total == target:
            found += 1   
        
        size = len(current)
        curTotal = total
        for i in range(size-1):
            curTotal -= current[i]
            if curTotal == target:
                found += 1
        left = self.getPaths(root.left,current,total,target)
        if root.left:
            total -= current.pop()
        right = self.getPaths(root.right,current,total,target)
        if root.right:
            current.pop()
        return found + left + right