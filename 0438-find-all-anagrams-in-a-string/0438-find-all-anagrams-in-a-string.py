from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = defaultdict(int)
        size = len(s)
        k = len(p)
        index = k-1
        result = []
        
        for char in p:
            target[char] += 1
            
        current = defaultdict(int)
        
        if k > size:
            return []
        for i in range(0,k-1):
            current[s[i]] += 1
            
        
        while index<size:
           
            current[s[index]] += 1
        
            if target == current:
                result.append(index-k+1)
                
            current[s[index-k+1]] -= 1
            
            if current[s[index-k+1]] == 0:
                del current[s[index-k+1]]
                
            index += 1
            # print(current,result)
            
        return result
            
        
        