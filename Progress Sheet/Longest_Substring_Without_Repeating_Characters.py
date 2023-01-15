class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        Max = 0
        i,j = 0,0
        dict = {}
        while(i < len(s)):
            if(j == len(s) or s[j] in dict ):
                Max = max(Max,j-i)
                dict = {}
                i+=1
                j = i
            else:
                dict[s[j]] = 1
                j+=1
        return Max
