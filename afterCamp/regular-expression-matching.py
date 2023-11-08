class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def matches(char1,char2):
            if char1 == "." or char2 == "." or char1 == char2:
                return True
            return False

        @cache
        def dp(i,j):
            if i == len(s) and j == len(p):
                return True            

            result = False

            if j+1 < len(p) and p[j+1] == '*':
                if i < len(s) and matches(s[i],p[j]):
                    result = result or dp(i+1,j) or dp(i+1,j+2)
                result = result or dp(i,j+2)
            else:
                if i < len(s) and j < len(p) and matches(s[i],p[j]):
                    result = result or dp(i+1,j+1)

            
            return result

        return dp(0,0)
        
