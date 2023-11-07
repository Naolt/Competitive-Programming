class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        @cache
        def dp(i,j):
            if i + j >= len(s3):
                return True

            result = False
            if i < len(s1) and s1[i] == s3[i+j]:
                result = result or dp(i+1,j)
            if j < len(s2) and s2[j] == s3[i+j]:
                result = result or dp(i,j+1)
            
            return result

        return False if len(s1)+len(s2) > len(s3) else dp(0,0)