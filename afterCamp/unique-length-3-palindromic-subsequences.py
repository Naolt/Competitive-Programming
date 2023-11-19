class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        def findDistinct(dic1,dic2):
            length = len(dic2)
            for key,value in dic1.items():
                if key in dic2:
                    if dic2[key] - value == 0:
                        length -= 1
            return length

        charDict = defaultdict(list)
        charCount = []
        chars = defaultdict(int)

        for index,char in enumerate(s):
            charDict[char].append(index)
            chars[char] += 1
            charCount.append(chars.copy())
        
        answer = 0
        palindormes = []
        for key,value in charDict.items():           
            if value[-1] - value[0] > 1:
                charsBetween = findDistinct(charCount[value[0]],charCount[value[-1]-1])
                answer += max(charsBetween,0)

        return answer