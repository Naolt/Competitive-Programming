class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        unionFind = UnionFind(len(strs))

        def checkDiff(str1,str2):
            count = 0

            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    count += 1
            
            return count

        for i in range(len(strs)):
            for j in range(len(strs)):
                if i != j:
                    diff = checkDiff(strs[i],strs[j])
                    if diff < 3:
                        unionFind.union(i,j)

        for i in range(len(strs)):
            unionFind.find(i)
        
        return len(set(unionFind.parent))


















class UnionFind:
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [0]*size
        self.count = size
        self.hasChild = [False for i in range(size)]

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
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root1] = root2
                self.rank[root2] += 1