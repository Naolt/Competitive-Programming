class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        nodeDict = {}
        for rich,poor in richer:
            graph[poor].append(rich)

        size = len(quiet)
        answer = []
        for i in range(size):
            result = self.dfs(graph,i,nodeDict,quiet)
            answer.append(result)

        return answer

    def dfs(self,graph,current,nodeDict,quiet):

        if current in nodeDict:
            return nodeDict[current]

        res = current

        for nbr in graph[current]:
            result = self.dfs(graph,nbr,nodeDict,quiet)
            if quiet[result] < quiet[res]:
                res = result

        nodeDict[current] = res
        
        return res