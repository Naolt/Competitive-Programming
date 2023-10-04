class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(dict)

        for start,end,weight in times:
            graph[start][end] = weight

        distances = {i+1:float('inf') for i in range(n)}
        distances[k] = 0
        p_queue = [(0,k)]
        visited = set()

        while p_queue:
            distance,node  = heappop(p_queue)

            if node in visited:
                continue
            visited.add(node)

            for neighbor,weight in graph[node].items():
                if distance + weight < distances[neighbor]:
                    distances[neighbor] = distance + weight
                    heappush(p_queue,(distance + weight,neighbor))

        result = max(distances.values())
        
        return result if result != float('inf') else -1