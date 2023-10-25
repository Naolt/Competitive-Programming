class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        elif n == -1:
            return 1/x

        half = self.myPow(x,n//2)
        result = half*half
        if n % 2:
            result *= x

        return result