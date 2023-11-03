class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin = prices[0]
        curMax = prices[0]
        profit = 0

        for price in prices:
            if price < curMin:
                curMin = price
                curMax = price
            else:
                curMax = price
            profit = max(profit,abs(curMax-curMin))
        
        return profit