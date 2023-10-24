class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        unionFind = UnionFind(26)
        lb,l1,l2 = len(baseStr),len(s1),len(s2)
        for i in range(l1):
            unionFind.union(s1[i],s2[i])
        
        result = ""

        for i in range(len(baseStr)):
            result += unionFind.find(baseStr[i])

        return result




class UnionFind:
    def __init__(self,size):
        self.parent = {chr(ord("a")+i):chr(ord("a")+i) for i in range(size)}
        self.rank = [0]*size
        self.count = size

    def find(self,member):
        root = member
        while root != self.parent[root]:
            root = self.parent[root]
        
        while member != root:
            parent = self.parent[member]
            self.parent[member] = root
            member = parent
        
        return root
    
    def union(self,member1,member2):
        root1 = self.find(member1)
        root2 = self.find(member2)

        if root1 != root2:
            if root1 > root2:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1