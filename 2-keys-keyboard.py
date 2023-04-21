class Solution:
    def minSteps(self, n: int) -> int:
        factors = self.getFactors(n)
        total = 0
        if factors[-1] != 1:
            factors.append(1)
        size = len(factors)
        for i in range(size-1):
            total += (factors[i]//factors[i+1])
        return total
        
    def getFactors(self,n):
        result = [n]
        while result[-1] > 2:
            for i in range(2,result[-1]+1):
                if not result[-1]%i:
                    result.append(result[-1]//i)
                    break
        return result