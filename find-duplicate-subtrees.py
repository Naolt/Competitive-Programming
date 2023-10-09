# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        dic = {}
        def findDup(node):
            if not node:
                return ""
            total = '|'
            total += findDup(node.left)
            total += '|'
            total += str(node.val)
            total += '|'
            total += findDup(node.right)
            
            if total in dic:
                dic[total][0] += 1
            else:
                dic[total] = [1,node]

            return total
        
        findDup(root)
        answer = []
        # print(len(dic))
        for key,[count,node] in dic.items():
            if count > 1:
                answer.append(node)
        return answer