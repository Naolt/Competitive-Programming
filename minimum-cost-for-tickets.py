class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        max_ = days[-1]
        daySet = set(days)
        @cache
        def dp(day):
            if day <= 0:
                return 0
    
            if day in daySet:
                cost1 = costs[0] + dp(max(day-1,0))
                cost2 = costs[1] + dp(max(day-7,0))
                cost3 = costs[2] + dp(max(day-30,0))
                return min(cost1,cost2,cost3)
            else:
                return dp(day-1)
           
        return dp(max_)