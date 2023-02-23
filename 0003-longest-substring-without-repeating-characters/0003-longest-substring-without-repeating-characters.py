class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        size = len(s)
        result = 0
        letterDict = {}
        for right in range(size):
            if s[right] in letterDict:
                left = max(letterDict[s[right]]+1,left)
    
            result = max(result,right-left+1)
            letterDict[s[right]] = right
               
        return result
                