class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        row = defaultdict(list)
        col = defaultdict(list)
        rep = {}
        size = {}

        for x,y in stones:
            row[x].append((x,y))
            col[y].append((x,y))
            rep[(x,y)] = (x,y)
            size[(x,y)] = 1


        graph = UnionFind(rep,size)

        for x,y in stones:
            for r,c in row[x]:
                graph.union((x,y),(r,c))
            for r,c in col[y]:
                graph.union((x,y),(r,c))
        
        visited = set()
        for key,value in graph.size.items():
            parent = graph.find(key)
            visited.add(parent)
        
        
        return len(stones)-len(visited)




class UnionFind:
    def __init__(self,rep,size):
        self.rep = rep
        self.size = size
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