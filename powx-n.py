class Solution:
    def myPow(self, x: float, n: int,first=False) -> float:

        if n == 1:
            return x
        if n == 0:
            return 1
        answer = self.myPow(x,math.floor(abs(n)/2))
        if n%2 != 0:
            result = x*answer*answer
            if n < 0:
                return 1/result
            return result
        else:
            result = answer*answer
            if n < 0:
                return 1/result
            return result