"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        return self.getDepth(root,1)
    def getDepth(self,root,depth):
        if not root.children:
            return depth
        maxDepth = 0
        for child in root.children:
            maxDepth = max(self.getDepth(child,depth+1),maxDepth)
            
        return maxDepth