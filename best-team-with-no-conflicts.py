class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        combined = list(zip(ages,scores))
        combined.sort(reverse=True)
        memo = defaultdict(int)
        size = len(scores)  
        answer = 0      
        for i in range(size):
            score = combined[i][1]
            memo[i] = score
            for j in range(i):
                if combined[j][1] >= score:
                    memo[i] = max(memo[i],memo[j]+score)
            
            answer = max(answer,memo[i])
        
        return answer