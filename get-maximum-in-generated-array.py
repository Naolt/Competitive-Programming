class Solution:
    def __init__(self):
        self.memo = {}
        self.max = 0
    def getMaximumGenerated(self, n: int) -> int:
        return self.bu(n)
        
        for i in range(n):
            self.dp(i+1)
        return self.max
    
    def dp(self, n: int) -> int:
        if n < 2:
            self.max = max(self.max,n)
            return n
        
        if n not in self.memo:
            current = 0
            if n % 2 == 0:
                current = self.dp(n//2)
            else:
                current = self.dp(n//2) + self.dp((n//2)+1)
            self.memo[n] = current
            self.max = max(self.max,current)

        return self.memo[n]

    def bu(self,n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        nums = [0]*(n+1)
        nums[1] = 1

        for i in range(1,n+1):
            if i*2 <= n:
                nums[i*2] += nums[i]
            if i*2+1 <= n:
                nums[i*2+1] = nums[i]+nums[i+1]
        
        return max(nums)