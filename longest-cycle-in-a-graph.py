class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        graph = {}
        for index,val in enumerate(edges):
            if val != -1:
                graph[index] = val
       
        size = len(edges)
        heights = [-1]

        # if len(superSet) < size:
            # heights[-1] = 1

        colors = [0]*size
        for i in range(size):
            if i in graph:
                self.dfs(graph,i,colors,heights)
        

        return heights[-1]

    def dfs(self,graph,current,colors,heights):
        if colors[current] == 2:
            return 
        if colors[current] == 1:
            print("current",current)
            heights[-1] = max(self.countCycleLen(graph,current,set()),heights[-1])
            return

        colors[current] = 1
        if graph[current] in graph:
            self.dfs(graph,graph[current],colors,heights)

        colors[current] = 2

    def countCycleLen(self,graph,current,visited):
        if current in visited:
            return len(visited)
        
        visited.add(current)
        
        return self.countCycleLen(graph,graph[current],visited)