class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1
        @cache
        def dp(a,b):
            # print(a,b)
            if a <= 0 and b <= 0:
                return 0.5
            if b <= 0:
                return 0
            if a <= 0:
                return 1

            total = 0
            total += dp(a-100,b)
            total += dp(a-75,b-25)
            total += dp(a-50,b-50)
            total += dp(a-25,b-75)

            return 0.25*total

        return dp(n,n)
            