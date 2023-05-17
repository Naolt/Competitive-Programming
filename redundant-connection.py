class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nums = {}

        for start,end in edges:
            nums[start] = 1
            nums[end] = 1
        
        graph = UnionSet(len(nums))

        for start,end in edges:
            if graph.onSamePath(start-1,end-1):
                return [start,end]
            graph.union(start-1,end-1)



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