"""
nums = [1,1,2,10000]
        i 
            j
  1  2
  1

approach:
   - 1 of the side can be greater than or equal to sum of the other sides
   - sum of the 2 smaller ones should be greater than the larger

"""

class Solution(object):
    
    def validArea(self,x,y,z):
        return x+y > z and x+z > y and y+z > x
    
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        size = len(nums)
        i = size-1
        j = size - 3
        maxPer = 0
        
        while( i > 0 and j >= 0 ):
            
          
            x,y,z = nums[i],nums[i-1],nums[j]
            
            if self.validArea(x,y,z):
                return x + y + z
            
            j-=1
            i-=1
            
            
        return 0
        