class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10**9 + 7)
        result = 1
        if n % 2 == 0:
            result *= (pow(5,n//2,mod) * pow(4,n//2,mod)) % mod
        else:
            result *= (pow(5,ceil(n/2),mod) * pow(4,n//2,mod)) % mod
       
        return result