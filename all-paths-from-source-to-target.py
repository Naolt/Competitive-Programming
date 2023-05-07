class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        self.backtrack(graph,0,len(graph)-1,[0],result)
        return result

    def backtrack(self,graph,idx,target,current,result):
        
        for edge in graph[idx]:
            current.append(edge)
            if edge == target:
                result.append(current[:])
                current.pop()
            else:
                self.backtrack(graph,edge,target,current,result)
                current.pop()