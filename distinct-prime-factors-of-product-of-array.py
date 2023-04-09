class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int: 
        total = set()
        for num in nums:
            factors = self.getFactors(num)
            total = total.union(factors)
        return len(total)
        
    def getFactors(self,number):
        factors = set()
        num = number
        for d in range(2,int(num**0.5)+1):
            if num % d == 0:
                factors.add(d)
            while num % d == 0:
                num //= d
        if num > 1:
            factors.add(num)
        
        return factors