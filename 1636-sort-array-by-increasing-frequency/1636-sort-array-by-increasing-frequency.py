from collections import defaultdict
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numDict = defaultdict(int) 
        result = []
        for index,num in enumerate(nums):
            numDict[num] += 1    
        values = list(numDict.values())
        key = list(numDict.keys())
        size = len(key)
        for i in range(size):
            for j in range(i+1,size):
                if values[i] > values[j]:
                    values[i], values[j] = values[j],values[i]
                    key[i], key[j] = key[j],key[i]
                elif values[i] == values[j]:
                    if key[i] < key[j]:
                        values[i], values[j] = values[j],values[i]
                        key[i], key[j] = key[j],key[i]
                        
                    
                    
        print(key,values)
        
        for i in range(size):
            for j in range(values[i]):
                result.append(key[i])
                
            
         
        
        
                    
        return result