class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for start,end in adjacentPairs:
            graph[start].append(end)
            graph[end].append(start)
            
        topSortedList = []
        for key,value in graph.items():
            if len(value) == 1:
                self.dfs(graph,key,topSortedList,set([key]))
                break
        
        return topSortedList

    def dfs(self,graph,current,array,visited):

        for nbr in graph[current]:
            if nbr not in visited:
                visited.add(nbr)
                self.dfs(graph,nbr,array,visited)
        array.append(current)