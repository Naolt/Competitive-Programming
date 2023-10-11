# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([(root,0)])
        size = 1
        while queue:
            s = len(queue)
            size = max(queue[-1][1]-queue[0][1]+1,size)

            for i in range(s):
                node,level = queue.popleft()
                if node.left:
                    queue.append((node.left,level*2+1))
                if node.right:
                    queue.append((node.right,level*2+2))

        return size