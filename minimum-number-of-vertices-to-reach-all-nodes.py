class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        lineInList = set()
        for start,end in edges:
            lineInList.add(end)
        result = []
        for vertex in range(n):
            if vertex not in lineInList:
                result.append(vertex)
        return result