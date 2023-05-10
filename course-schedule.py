class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        incoming = [0]*numCourses
        nodeGraph = defaultdict(list)
        noIncoming = []

        for start, end in prerequisites:
            nodeGraph[end].append(start)
            incoming[start] += 1

        for key,value in enumerate(incoming):
            if value == 0:
                noIncoming.append(key)
        
        colors = [0] * (numCourses+1)
        # print(noIncoming)
        for node in range(numCourses):
            cycleFound = self.hasCycle(node,colors,nodeGraph)
            if cycleFound:
                return False
        return True



    def hasCycle(self,currentNode,colors,nodeGraph):

        if colors[currentNode] == 2:
            return False
        
        if colors[currentNode] == 1:
            return True

        colors[currentNode] = 1

        for neighbour in nodeGraph[currentNode]:
            cycleFound = self.hasCycle(neighbour,colors,nodeGraph)
            if cycleFound:
                return True
        # topSortedOrder.append(currentNode)
        colors[currentNode] = 2
        return False