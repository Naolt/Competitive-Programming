class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for start,end in roads:
            graph[start].append(end)
            graph[end].append(start)
        
        sortedGraph = sorted(graph,key=lambda x:len(graph[x]),reverse = True)
        roadsSelected = set()
        if not roads:
            return 0
        currMax = 0

        for i in range(n):
            for j in range(n):
                currMax = max(currMax,self.getRank(graph,i,j))
                
        return currMax

    def getRank(self,graph,first,second):
        setFirst = set()
        setSecond = set()
        for neighbour in graph[first]:
            setFirst.add((first,neighbour))
        for neighbour in graph[second]:
            if (second,neighbour) not in setFirst and (neighbour,second) not in setFirst:
                setSecond.add((second,neighbour))
        return len(setFirst.union(setSecond))
        

        # for neigbour in first:
        #     if (sortedGraph[0],neigbour) not in roadsSelected and (neigbour,sortedGraph[0]) not in roadsSelected:
        #         roadsSelected.add((sortedGraph[0],neigbour))
        # for neigbour in second:
        #     if (sortedGraph[1],neigbour) not in roadsSelected and (neigbour,sortedGraph[1]) not in roadsSelected:
        #         roadsSelected.add((sortedGraph[1],neigbour))
        # print(roadsSelected,sortedGraph)     
        # return len(roadsSelected)