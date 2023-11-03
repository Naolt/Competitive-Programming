class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        countList = list(count.items())
        countList.sort(key=lambda x:x[1], reverse=True)

        indices = defaultdict(list)

        for index,num in enumerate(nums):
            indices[num].append(index)
        
        key,freq = countList[0]
        minSize = indices[key][-1]+1 - indices[key][0]

        for i in range(1,len(countList)):
            newKey,newFreq = countList[i]
            if newFreq != freq:
                break
            minSize = min(minSize,indices[newKey][-1]+1 - indices[newKey][0])

        return minSize



        


