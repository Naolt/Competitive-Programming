class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming = [0]*n
        for start,end in edges:
            graph[start].append(end)
            graph[end].append(start)
            incoming[start] += 1
            incoming[end] += 1
        
        queue = deque()
        for key,value in enumerate(incoming):
            if value <= 1:
                queue.append(key)
        last = []
        while len(queue) > 1:
            size = len(queue)
            last = list(queue)
            for i in range(size):
                node = queue.popleft()

                for nbr in graph[node]:
                    incoming[nbr] -= 1
                    if incoming[nbr] == 1:
                        queue.append(nbr)

        return last if not queue else queue