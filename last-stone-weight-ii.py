class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        @cache
        def dp(index,tot):
            if index == len(stones):
                return tot
            
            neg = dp(index+1,abs(tot-stones[index]))
            pos = dp(index+1,abs(tot+stones[index]))

            return min(neg,pos)
        
        return dp(0,0)