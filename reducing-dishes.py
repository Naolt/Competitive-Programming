class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)

        tot = 0
        ans = 0 
        for s in satisfaction:
            ans += s
            if ans <= 0:
                break
            tot += ans
        
        return tot