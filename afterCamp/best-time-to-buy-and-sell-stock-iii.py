class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def dp(index,count,buy):
            if count >= 2:
                return 0
            if index == len(prices)-1:
                return 0 if buy else prices[index]

            included,notIncluded = 0,0
            if buy:
                included = -prices[index] + dp(index+1,count,False)
                notIncluded = dp(index+1,count,True)
                return max(included,notIncluded)
            else:
                included = prices[index] + dp(index+1,count+1,True)
                notIncluded = dp(index+1,count,False)
                return max(included,notIncluded)
        
        return dp(0,0,True)

            