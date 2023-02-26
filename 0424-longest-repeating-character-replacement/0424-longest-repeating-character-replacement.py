"""
AABABBA   k = 1
l
 r


"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letterDict = collections.defaultdict(int)
        size = len(s)
        left = 0
        currMax = 0
        result = 0
        
        for i in range(size+1):
            result = max(result,i-left)
            if i >= size:
                break
            letterDict[s[i]] += 1
            if currMax not in letterDict:
                currMax = s[i]
            else:
                if letterDict[s[i]] > letterDict[currMax]:
                    currMax = s[i]
            if i+1-left - letterDict[currMax] > k:
                # print("deleteing",s[left],letterDict[currMax],i)
                result = max(result,i-left)
                letterDict[s[left]] -= 1
                if letterDict[s[left]] == 0:
                    del letterDict[s[left]]
                left += 1
            # print(result,currMax,left,i,letterDict)
            
        return result
        