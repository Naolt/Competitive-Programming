class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        window = s[0:10]
        # for i in range(10):
        #     window[s[i]] += 1
        size = len(s)
        countDict = defaultdict(int)
        countDict[window] += 1


        for i in range(10,size):
            window = window[1:] + s[i]
            countDict[window] += 1

        result = []
        for key,value in countDict.items():
            if value > 1:
                result.append(key)
        return result