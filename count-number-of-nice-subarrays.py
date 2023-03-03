class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = []
        for num in nums:
            if num % 2 == 0:
                prefix.append(0)
            else:
                prefix.append(1)
        prefix = list(accumulate(prefix))
        numDict = collections.defaultdict(int)
        numDict[0] = 1
        result = 0
        for num in prefix:
            if num-k in numDict:
                result += numDict[num-k]
            numDict[num] += 1
        return result