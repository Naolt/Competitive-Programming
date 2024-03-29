# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        return self.bfs(root,root)
    
    def bfs(self,graph, node):
        visited = set([node])
        queue = deque([node])
        result = []
        while queue:
            size = len(queue)
            total = 0
            for i in range(size):
                node = queue.popleft()
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(total/size)
        return result