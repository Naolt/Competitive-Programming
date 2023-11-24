class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getHash(word):
            word_sorted = sorted(list(word))
            hashed = 0
            for i in range(len(word)):
                hashed *= 26
                hashed += 26*ord(word_sorted[i])

            return hashed
        
        hashDic = defaultdict(list)
        for word in strs:
            hashDic[getHash(word)].append(word)
        
        return hashDic.values()

            
        