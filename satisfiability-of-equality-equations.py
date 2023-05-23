class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        graph = UnionSet(0)
        notEqual = []
        visited = set()
        for equation in equations:
            
            start,sign,_,end = list(equation)
            if sign == "=":
                graph.union(ord(start),ord(end))
            else:
                notEqual.append((ord(start),sign,ord(end)))

        for start,sign,end in notEqual:
            if graph.find(start) == graph.find(end):
                return False                

        return True












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