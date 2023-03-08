# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        return self.getPath(root,"",[])
        
    def getPath(self,root,s,arr):
        print(root)
        if not root:
            return arr
        if s == "":
            s += str(root.val)
        else:
            s += ("->" +str(root.val))

        if not root.right and not root.left:
            arr.append(s)
            return arr 
        self.getPath(root.left,s,arr)
        self.getPath(root.right,s,arr)
        return arr