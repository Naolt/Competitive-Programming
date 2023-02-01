class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        word1 = list(word1)
        word2 = list(word2)
        merge = ""
        print(word1,word2)
        while len(word1) > 0 and len(word2) > 0:
            if word1 > word2:
                merge += word1.pop(0)
            else:
                merge += word2.pop(0)
        
        
        
        return (merge + "".join(word1) + "".join(word2))
        
        