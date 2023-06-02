class Solution:
    def __init__(self):
        self.memo = {}
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        start = nums[0:len(nums)-1]
        val1 = self.dp(start,0,0)
        self.memo = {}
        end = nums[1:len(nums)]
        val2 = self.dp(end,0,0)
        return max(val1,val2)

    def dp(self,nums,idx,sums):
        if idx >= len(nums):
            return sums
        if idx in self.memo:
            return self.memo[idx]
        val = max(self.dp(nums,idx+2,sums)+nums[idx],self.dp(nums,idx+1,sums))

        self.memo[idx] = val

        return val