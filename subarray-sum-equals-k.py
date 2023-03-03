class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        size = len(nums)
        numDict = defaultdict(int)
        numDict[0] = 1
        prefix = list(accumulate(nums))
        result = 0
        for num in prefix:
            if num-k in numDict:
                result += numDict[num-k]
            numDict[num] += 1
        
        return result