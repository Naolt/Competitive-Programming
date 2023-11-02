class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1]*len(nums)

        for index,num in enumerate(nums):
            currentMax = 0
            for i in range(index-1,-1,-1):
                if nums[i] < num:
                    currentMax = max(currentMax,dp[i])
            dp[index] += currentMax

        
        return max(dp)