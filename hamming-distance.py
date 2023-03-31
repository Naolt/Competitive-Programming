class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        for i in range(32):
            if (x & (2**i)) != (y & (2**i)):
                count += 1
        return count