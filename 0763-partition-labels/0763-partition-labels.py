class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size = len(s)
        charDict = {}
        for i in range(size-1,-1,-1):
            if s[i] not in charDict:
                charDict[s[i]] = i
        
        left = 0
        right = size-1
        count = 0
        result = []
        
        while left < size:
            right = charDict[s[left]]
            #check if the char at left index is same to the dict
            
            i = left + 1   
            while i < right:
                if charDict[s[i]] > right:
                    right = charDict[s[i]]
                i +=1
            if left == size:
                result.append(count)
            else:
                result.append(right-left+1+count)
            count = 0
            left = right + 1
        return result
                
                