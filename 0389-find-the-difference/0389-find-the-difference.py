from collections import defaultdict
"""
s = "abbcd", t = "abcdbb"
dict = {a:1,b:2,c:1:d:1}
 
 
approach:
    -construct a dictionary to hold the letters and their frequency of letters on s
    -then check the presence of each letters from t on the dict if not return that letter
    - if the letter is found substract 1 from the frequency if the letter is present and frequency is 0 return that number


"""



class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        dictn = defaultdict(int)
        for char in s:
            dictn[char] +=1
        
        for char in t:
            if not bool(dictn[char]):
                return char
            else:
                dictn[char] -=1
            