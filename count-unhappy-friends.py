class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        rank = [[float('inf')]*n for i in range(n)]
        allPairs = pairs[::]
        for i,pref in enumerate(preferences):
            for j,value in enumerate(pref):
                rank[i][value] = j+1
        for pair in pairs:
            allPairs.append(pair[::-1])
        
        unhappy = set()
        for f1,f2 in allPairs:
            score = rank[f1][f2]
            if score > 1:
                for n1,n2 in allPairs:
                    currScore = rank[n1][n2]
                    if rank[f1][n1] < score and rank[n1][f1] < currScore:
                        unhappy.add(f1)
                        unhappy.add(n1)
        
        return len(unhappy)