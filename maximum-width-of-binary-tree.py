# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.left = -1
        self.right = -1
        self.i = 0

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDepth = max(self.getDepth(root.left),self.getDepth(root.right))+1
        def getWidth(root,depth,maxDepth):
            if depth == 1:
                if root:
                    if self.left < 0:
                        self.left = self.i
                    else:
                        self.right = self.i
                    self.i += 1
                else:
                    self.i += 1
            else:
                if not root:
                    self.i += 2**(maxDepth-(maxDepth-depth+1))
                else:
                    getWidth(root.left,depth-1,maxDepth)
                    getWidth(root.right,depth-1,maxDepth)

        currentMax = 0
        for i in range(1,maxDepth+1):
            result = getWidth(root,i,i)
            if (self.left < 0 or self.right < 0 ) and not (self.left < 0 and self.right < 0):
                currentMax = max(currentMax,1)
            elif self.left >= 0 and self.right >=0:
                currentMax = max(currentMax,self.right-self.left+1)
            self.left = -1
            self.right = -1
            self.i = 0
        return currentMax 
    def getDepth(self,root):
        if not root:
            return 0
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)

        return max(left,right)+1