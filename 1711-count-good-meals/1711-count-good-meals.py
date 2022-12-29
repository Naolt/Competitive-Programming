"""
dict = {
2,4,8,16
}



"""

import math

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
        count = 0
        size = len(deliciousness)
        numDict = {} 
        countDict = {}
        for i in range(22):
            numDict[2**i] = 1
        
        for value in deliciousness:
            
            if value in countDict:
                count += countDict[value]
                
            for sum in numDict:
                element = sum - value
                if element not in countDict:
                    countDict[element] = 1
                else:
                    countDict[element] += 1
            # print(numDict) 
        
        return count % (10**9 +7)