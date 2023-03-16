# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        def traverse(root,dic,row,col):
            if not root:
                return
            dic[col].append([row,root.val])
            traverse(root.left,dic,row+1,col-1)
            traverse(root.right,dic,row+1,col+1)

        traverse(root,dic,0,0)
        sortedDic = sorted(dic)
        result = []
        for key in sortedDic:
            newVal = sorted(dic[key])
            current = []
            for val in newVal:
                current.append(val[1])
            result.append(current)
        return result