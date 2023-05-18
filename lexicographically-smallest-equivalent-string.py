class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = UnionSet(0)
        length = len(s1)

        for i in range(length):
            graph.union(ord(s1[i]),ord(s2[i]))
        

        result = ""

        for char in baseStr:
            result += chr(graph.find(ord(char)))

        return result










class UnionSet:
    def __init__(self,size):
        self.rep = {97+i:97+i for i in range(26)}
        # self.size = {i:1 for i in range(size)}

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

        if rep1 < rep2:
            # self.size[rep1] += self.size[rep2]
            self.rep[rep2] = rep1
        else:
            # self.size[rep2] += self.size[rep1]
            self.rep[rep1] = rep2
    
    def onSamePath(self,num1,num2):
        rep1 = self.find(num1)
        rep2 = self.find(num2)

        return rep1 == rep2