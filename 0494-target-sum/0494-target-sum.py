class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = {}
        def calculate(index,total):
            if index >= len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            
            if (index,total) not in memo:
                add = calculate(index+1,total+nums[index])
                sub = calculate(index+1,total-nums[index])
                memo[ (index,total) ] = add+sub
        
            return memo[(index,total)]
        
        return calculate(0,0)