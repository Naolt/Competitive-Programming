class Solution:
    def myPow(self, x: float, n: int,first=False) -> float:

        if n == 1:
            return x
        if n == 0:
            return 1
        answer = self.myPow(x,math.floor(abs(n)/2))
        result = answer*answer
        if n%2 != 0:
            if n < 0:
                return 1/(x*result)
            return x*result
        else:
            if n < 0:
                return 1/result
            return result