class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # For recursive dfs and iterative 

        # graph = defaultdict(list)
        # for start,end in edges:
        #     graph[start].append(end)
        #     graph[end].append(start)

        # return self.dfs(graph,source,set(),destination)
        # return self.iterative(graph,source,destination)

        # For union 

        graph = UnionSet(n)

        for start,end in edges:
            graph.union(start,end)
        
        return graph.onSamePath(source,destination)


    def dfs(self,graph,vertex,visited,destination):
        if vertex == destination:
            return True
        visited.add(vertex)
        found = False
        for node in graph[vertex]:
            if node not in visited: 
                found = found or self.dfs(graph,node,visited,destination)
        return found
    
    def iterative(self,graph,start,destination):
        stack = [start]
        visited = set()

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                stack.extend(graph[node])
        return False
    


class UnionSet:
    def __init__(self,size):
        self.rep = {i:i for i in range(size)}
        self.size = {i:1 for i in range(size)}

    def find(self,num):
        root = num
        while root != self.rep[root]:
            root = self.rep[root]
        
        while num != self.rep[num]:
            parent = self.rep[num]
            self.rep[num] = root
            num = parent
        
        return root

    def union(self,num1,num2):
        rep1 = self.find(num1)
        rep2 = self.find(num2)

        if rep1 == rep2:
            return

        if self.size[rep1] > self.size[rep2]:
            self.size[rep1] += self.size[rep2]
            self.rep[rep2] = rep1
        else:
            self.size[rep2] += self.size[rep1]
            self.rep[rep1] = rep2
    
    def onSamePath(self,num1,num2):
        rep1 = self.find(num1)
        rep2 = self.find(num2)

        return rep1 == rep2