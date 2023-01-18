from collections import defaultdict
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        commonDict = defaultdict(int)
        size = len(words)
        
        for letter in words[0]:
            commonDict[letter] += 1
            
        for i in range(1,size):
            tempDict = defaultdict(int)
            
            for letter in words[i]:
                tempDict[letter] += 1
                
            keys = list(commonDict.keys())
            
            for key in keys:
                if key not in tempDict:
                    commonDict.pop(key)
                elif tempDict[key] < commonDict[key]:
                    commonDict[key] = tempDict[key]
        
        result = []
        for key,value in commonDict.items():
            for i in range(value):
                result.append(key)
        return result 
        