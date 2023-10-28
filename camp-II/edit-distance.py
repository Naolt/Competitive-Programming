class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @cache
        def dp(i,j):
            if i == len(word1):
                # Option 3: insert the rest of the character
                return len(word2) - j
            if j == len(word2):
                # Option 2: delete the rest of the character
                return len(word1) - i
            
            if word1[i] != word2[j]:
                # option 1: Replace
                replace = 1 + dp(i+1,j+1)
                # option 2: Delete
                delete = 1 + dp(i+1,j)
                # option 3: Insert
                insert = 1 + dp(i,j+1)

                return min(replace,delete,insert)
            
            return dp(i+1,j+1)

        return dp(0,0)

