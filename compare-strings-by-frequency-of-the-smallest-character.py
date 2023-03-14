class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        newWords = []
        for word in words:
            newWords.append(self.getSmallerFreq(word))
        newWords.sort()
        print(newWords)
        size = len(words)
        result = []
        for query in queries:
            left = -1
            right = len(words)
            current = self.getSmallerFreq(query)
            while left+1 < right:
                middle = math.floor(left + (right-left)/2)

                if newWords[middle] <= current:
                    left = middle
                else:
                    right = middle
            result.append(size-left-1)
        return result

    def getSmallerFreq(self,word):
        dic = Counter(word)
        sortedDic = sorted(dic)
        return dic[sortedDic[0]]