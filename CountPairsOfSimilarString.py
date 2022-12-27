"""
words = ["aba","aabb","abcd","bac","aabc"]
                         i    j
dict = {a:1,b:1}
count = 1

"""
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        count = 0
        size = len(words)
        for i in range(1,size):
            j = i-1
            setA = set(list(words[j]))
            
            for k in range(i,size):
                setB = set(list(words[k]))        
                
                if len(setA | setB) == len(setA) and len(setA | setB) == len(setB):
                    count +=1
        return count
