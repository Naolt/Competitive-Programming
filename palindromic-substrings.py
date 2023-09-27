class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        size = len(s)
        dp = [[0]*size for i in range(size)]

        for right in range(size-1,-1,-1):
            for left in range(right,size):
                
                if  s[right] == s[left] and (left-right < 3 or dp[right+1][left-1]):
                    dp[right][left] += 1
                else:
                    dp[right][left] = 0

                total += dp[right][left]
        return total