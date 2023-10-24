class UnionFind:
    def __init__(self,size):
        self.parent = [i for i in range(size)]
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
            if root1 == 0 or self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif root2 == 0 or self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root1] = root2
                self.rank[root2] += 1


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        unionFind = UnionFind(n)
        unionFind.parent[firstPerson] = 0
        unionFind.rank[0] = 1

        meetings.sort(key=lambda x:x[2])
        meetingDic = defaultdict(list)
        for x,y,t in meetings:
            meetingDic[t].append([x,y])
          
        sortedDic = sorted(meetingDic)

        for key in sortedDic:
            dicMeetings = meetingDic[key]
            for x,y in dicMeetings:
                unionFind.union(x,y)
            for x,y in dicMeetings:
                parentX = unionFind.find(x)
                parentY = unionFind.find(y)
                if parentX != 0:
                    unionFind.parent[x] = x
                    unionFind.rank[parentX] -= 1
                if parentY != 0:
                    unionFind.parent[y] = y
                    unionFind.rank[parentY] -= 1
                



        
        result = []
        for index,val in enumerate(unionFind.parent):
            if val == 0:
                result.append(index)

        return result