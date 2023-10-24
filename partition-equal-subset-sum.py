class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)/2
        
        @cache
        def dp(index,total):
            if total == sum_:
                return True

            if index >= len(nums) or total > sum_:
                return False
    
            return dp(index+1,total+nums[index]) or dp(index+1,total)

        return dp(0,0)