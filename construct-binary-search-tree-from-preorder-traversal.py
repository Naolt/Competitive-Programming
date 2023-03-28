# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = None
        for num in preorder:
            root = self.insertNode(root,num)
        return root
        

    def insertNode(self,root,val):
        if not root:
            return TreeNode(val,None,None)

        if root.val < val:
            root.right = self.insertNode(root.right,val)
        else:
            root.left = self.insertNode(root.left,val)
        
        return root