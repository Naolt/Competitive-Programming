# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if (not root or not root.left or (not root.left.left and not root.left.right) )and (not root or not root.right or (not root.right.right and not root.right.left) ):
            return 0
        evenSum = 0
        if root.val % 2 == 0:
            if  root.left: 
                if root.left.left:
                    evenSum += root.left.left.val
                if root.left.right:
                    evenSum += root.left.right.val
            if  root.right:
                if root.right.right:
                    evenSum += root.right.right.val
                if root.right.left:
                    evenSum += root.right.left.val
        return evenSum + self.sumEvenGrandparent(root.right) + self.sumEvenGrandparent(root.left)