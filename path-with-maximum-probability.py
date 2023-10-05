class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(dict)

        for index,[start,end] in enumerate(edges):
            graph[start][end] = succProb[index]
            graph[end][start] = succProb[index]
        
        distance = [0 for i in range(n)]
        distance[start_node] = 1
        heap = [(1,start_node)]
        visited = set()

        while heap:
            prob,node = heappop(heap)
            if prob < 0:
                prob *= -1
            if node in visited:
                continue
            visited.add(node)
            for nbr,w in graph[node].items():
                if prob * w > distance[nbr]:
                    distance[nbr] = prob*w
                    heappush(heap,(-1*(prob*w),nbr))
        return distance[end_node]