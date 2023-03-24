class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        totalSum = (size*(size+1))//2
        listSum = sum(nums)
        return totalSum-listSum