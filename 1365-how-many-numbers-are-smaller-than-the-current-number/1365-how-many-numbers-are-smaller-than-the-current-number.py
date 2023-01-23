class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        result = []
        size = len(nums)
        
        for i in range(size):
            noSmaller = 0
            for j in range(size):
                if nums[j]<nums[i]:
                    noSmaller += 1
            result.append(noSmaller)
        return result