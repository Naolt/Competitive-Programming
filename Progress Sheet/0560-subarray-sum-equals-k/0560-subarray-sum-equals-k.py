class Solution(object):
    def subarraySum(self, nums, k):
        result = 0
        prefixCount = {0: 1}
        currentSum = 0
        for num in nums:
            currentSum += num
            kDiff = currentSum - k
            result += prefixCount.get(kDiff, 0)
            prefixCount[currentSum] = 1 + prefixCount.get(currentSum, 0)
        return result
        