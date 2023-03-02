class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for i in range(1,size):
            nums[i] += nums[i-1]
        return nums