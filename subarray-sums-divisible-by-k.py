class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        numDict = defaultdict(int)
        numDict[0] = 1
        result = 0
        prefix = 0

        for num in nums:
            prefix += num 
            if prefix % k in numDict:
                result += numDict[(prefix%k)]
            numDict[prefix%k] += 1
        return result