# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        graph = defaultdict(list)
        self.getEdges(root,graph)
        print(graph)
        queue = deque([target.val])
        visited = set([target.val])
        count = 0

        while queue:
            size = len(queue)
            if count == k:
                return list(queue)
            for i in range(size):
                node = queue.popleft()
                print("popped",node,'childs',graph[node],'visited',visited)
                for child in graph[node]:
                    print("visited",child in visited)
                    if child not in visited:
                        print(child)
                        queue.append(child)
                        visited.add(child)
            
            count += 1

        return []


    def getEdges(self,root,graph):
        # print(root.val if root else None)
        if not root:
            return
        if root.right:
            graph[root.val].append(root.right.val)
            graph[root.right.val].append(root.val)
        if root.left:
            graph[root.val].append(root.left.val)
            graph[root.left.val].append(root.val)
        self.getEdges(root.left,graph)
        self.getEdges(root.right,graph)