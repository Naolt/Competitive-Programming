class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = {}
        def dp(current):
            if current >= target:
                if current > target:
                    return 0
                return 1
            
            if current not in memo:
                found = 0
                for num in nums:
                    found += dp(current+num)
                memo[current] = found
            
            return memo[current]
        return dp(0)