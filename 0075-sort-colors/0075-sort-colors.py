"""
[0,0,2,1,1,2]
 i
         j
 k

"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zero = 0
        two = len(nums)-1
        size = len(nums)
    
        for i in range(size):
            for j in range(size-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
            
            
                
            