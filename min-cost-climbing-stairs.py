class Solution:
    def __init__(self):
        self.memo = {}
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        ans = self.dp(cost,0)
        self.memo = {}
        ans2 = self.dp(cost,1)
        
        return min(ans,ans2)

    def dp(self,cost,idx):
        if idx >= len(cost):
            return 0
        if idx == len(cost)-1:
            return cost[idx]
        
        if idx in self.memo:
            return self.memo[idx]
        
        first = self.dp(cost,idx+1)
        second = self.dp(cost,idx+2)

        self.memo[idx] = min(second+cost[idx],first+cost[idx]) 

        return self.memo[idx]