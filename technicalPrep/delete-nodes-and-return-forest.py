# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        to_delete.add(-1)
        answer = []

        def findRoots(root,parent):
            if not root:
                return None
            if parent in to_delete and root.val not in to_delete:
                answer.append(root)
            
            findRoots(root.left,root.val)
            findRoots(root.right,root.val)
        
        def deleteChild(root):
            if not root:
                return None
            if root.left and root.left.val in to_delete:
                root.left = None
            if root.right and root.right.val in to_delete:
                root.right = None
            root.left = deleteChild(root.left)
            root.right = deleteChild(root.right)

            return root
        
        findRoots(root,-1)
        result = []
        for rootNode in answer:
            result.append(deleteChild(rootNode))
        
        return result
            

