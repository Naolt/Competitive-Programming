class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        maxLength = 0
        size = len(s)
        dp = [[0]*size for i in range(size)]
        
        for i in range(size-1,-1,-1):
            for j in range(i,size):

                if s[i] == s[j] and (j - i + 1 < 3 or dp[i+1][j-1]):
                    if (j-i+1) < 3:
                        dp[i][j] = j-i+1
                        maxLength = max(maxLength,j-i+1)
                    else:
                        dp[i][j] = dp[i+1][j-1] + 2
                        maxLength = max(maxLength,dp[i][j])
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i+1][j])
        return maxLength