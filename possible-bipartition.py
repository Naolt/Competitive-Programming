class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        set1 = set()
        set2 = set()
        green,red = 1,-1
        graph = defaultdict(list)
        for start,end in dislikes:
            graph[start].append(end)
            graph[end].append(start)
        colorDict = defaultdict(int)
        for person in range(1,n+1):
            if colorDict[person] == 0 and not self.setColor(green,person,graph,colorDict):
                return False
        return True


    def setColor(self,color,person,graph,colorDict):
        green,red = 1,-1

        colorDict[person] = color
        
        for dislike in graph[person]:
            
            if colorDict[dislike] == color:
                return False
            if colorDict[dislike] == 0 and not self.setColor(-color,dislike,graph,colorDict):
                return False

        return True