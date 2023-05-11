class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        incoming = [0]*n
        nodeGraph = defaultdict(list)
        queue = deque([])

        for start, end in edges:
            nodeGraph[start].append(end)
            incoming[end] += 1

        for key,value in enumerate(incoming):
            if value == 0:
                queue.append(key)
        
        result = [set() for i in range(n)]
        topSortOrder = []
        while queue:
            currentNode = queue.popleft()
            topSortOrder.append(currentNode)
            for neighbour in nodeGraph[currentNode]:
                result[neighbour].add(currentNode)
                result[neighbour] = result[neighbour].union(result[currentNode])
                incoming[neighbour] -= 1

                if incoming[neighbour] == 0:
                    queue.append(neighbour)
        result2 = []
        for arr in result:
            result2.append(sorted(arr))
        return result2