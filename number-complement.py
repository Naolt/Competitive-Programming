class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        count = 0

        while num > 0:
            temp = 0
            temp += int(not(num & 1))
            temp <<= count
            ans += temp
            count += 1
            num >>= 1 
        return ans
100