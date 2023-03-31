class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        # for i in range(32):
        #     if (x & (2**i)) != (y & (2**i)):
        #         count += 1
        while x or y:
            if (x^y)&1:
                count += 1
            x>>=1
            y>>=1
        return count