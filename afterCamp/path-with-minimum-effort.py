from queue import PriorityQueue
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        direc = [[0,1],[1,0],[0,-1],[-1,0]]
        d = defaultdict(int)
        def inbound(i,j):
            return 0 <= i < len(heights) and 0<= j <len(heights[0])
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                d[(i,j)] = float('inf')
                for x, y in direc:
                    if inbound(x+i,j+y):
                        dis =abs(heights[i][j] - heights[x+i][j+y])
                        graph[(i,j)].append([dis,(x+i,j+y)])
        heap = [(0,(0,0))]
        
        d[(0,0)] = 0

        while heap:
            w, dis = heappop(heap)
            if dis in visited:
                continue
            visited.add(dis)
            for nw,negi in graph[dis]:
                new_dis = max(w ,nw)
                if new_dis < d[negi]:
                    d[negi] = new_dis
                    heappush(heap,(new_dis,negi))

        return d[(len(heights)-1,len(heights[0])-1)]
