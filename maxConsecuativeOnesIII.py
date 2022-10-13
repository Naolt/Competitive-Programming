class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m, beg = len(nums), 0
        
        for end in range(m):
            
            if nums[end] == 0:
                k -= 1
            
            if k < 0:
                if nums[beg] == 0:
                    k += 1
                beg += 1
        
        return end - beg + 1
