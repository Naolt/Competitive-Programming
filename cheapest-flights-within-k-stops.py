class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        def dijkstra(graph, start, end, n, k):
            distances = {i: (float('inf'), float('inf')) for i in range(n)}
            distances[start] = (0, -1)
            priority_queue = deque([(0, -1, start)])

            while priority_queue:
                current_distance, val, current_vertex = priority_queue.popleft()
                if val >= k:
                    continue

                for neighbor, price in graph[current_vertex]:
                    distance = current_distance + price

                    if distance < distances[neighbor][0]:
                        distances[neighbor] = (distance, val + 1)
                        priority_queue.append((distance, val + 1, neighbor))

            if distances[end][1] <= k:
                return distances[end][0]
            return -1
        
        graph = defaultdict(list)
        for source, target, time in flights:
            graph[source].append([target, time])

        return dijkstra(graph, src, dst, n, k)