class Solution:
    def __init__(self):
        self.memo = {}
        self.max = 0
    def getMaximumGenerated(self, n: int) -> int:
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