class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graphLength = len(graph)
        incoming = [0]*graphLength
        nodeGraph = defaultdict(list)
        noIncoming = []

        for index,neighbours in enumerate(graph):
            for neighbour in neighbours:
                nodeGraph[index].append(neighbour)
                incoming[neighbour] += 1

        for key,value in enumerate(incoming):
            if value == 0:
                noIncoming.append(key)
        
        topSortedOrder = []
        colors = [0] * (graphLength+1)
        # print(noIncoming)
        for node in range(graphLength):
            cycleFound = self.hasCycle(node,colors,nodeGraph,topSortedOrder)
        topSortedOrder.sort()
        return topSortedOrder



    def hasCycle(self,currentNode,colors,nodeGraph,topSortedOrder):

        if colors[currentNode] == 2:
            return False
        
        if colors[currentNode] == 1:
            return True

        colors[currentNode] = 1

        for neighbour in nodeGraph[currentNode]:
            cycleFound = self.hasCycle(neighbour,colors,nodeGraph,topSortedOrder)
            if cycleFound:
                return True
        topSortedOrder.append(currentNode)
        colors[currentNode] = 2
        return False