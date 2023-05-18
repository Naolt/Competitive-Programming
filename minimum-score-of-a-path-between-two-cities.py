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


        if self.size[rep1] >= self.size[rep2]:
            self.size[rep1] += self.size[rep2]
            self.rep[rep2] = rep1

        else:
            self.size[rep2] += self.size[rep1]
            self.rep[rep1] = rep2

    
    def onSamePath(self,num1,num2):
        rep1 = self.find(num1)
        rep2 = self.find(num2)

        return rep1 == rep2

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = UnionSet(n)
        currMin = {i:float('inf') for i in range(n)}

        for start,end,distance in roads:
            startD,endD = currMin[graph.find(start-1)],currMin[graph.find(end-1)]
            graph.union(start-1,end-1)
            currMin[graph.find(start-1)] = min(startD,endD,distance)
        

        return currMin[graph.find(0)]