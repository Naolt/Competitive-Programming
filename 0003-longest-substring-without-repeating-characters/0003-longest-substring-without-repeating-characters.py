class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right = 0,0
        size = len(s)
        result = 0
        letterDict = {}
        while right < size:
            print(result)
            if s[right] not in letterDict:
                letterDict[s[right]] = 1
                right += 1
                result = max(result,right-left)
            else:
                del letterDict[s[left]]
                left += 1
                
        return result
                