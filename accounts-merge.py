class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        nameDict = defaultdict(str)
        rep = {}
        size = {}

        for account in accounts:
            length = len(account)

            for i in range(1,length):
                rep[account[i]] = account[i] 
                size[account[i]] = 1
                nameDict[account[i]] = account[0]
        
        graph = UnionFind(rep,size) 

        for account in accounts:
            size = len(account)
            for i in range(1,size-1):
                graph.union(account[i],account[i+1])
        
        result = defaultdict(list)

        for email,value in rep.items():

            parent = graph.find(email)
            result[parent].append(email)
        
        finalResult = []

        for key,value in result.items():
            row = []
            row.append(nameDict[key])
            row.extend(sorted(value))
            finalResult.append(row)

        return finalResult


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