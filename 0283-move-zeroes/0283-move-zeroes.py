"""
nums = [1,1,0,3,12]
          
          j
                
approach:
- first iterator searches for zero and second iterator searches for number other than zero
- if the first iterator founds zero the second iterator searches for number if it founds number they swap 
value and again i will be searching for zero and same happens until the end

"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        zeroIndex = 0
        numIndex = 0
        
        left = 0
        for i in range(size):
            if nums[i] != 0:
                nums[i],nums[left] = nums[left],nums[i]
                left +=1
        
#         while zeroIndex < size and numIndex < size:
            
#             while  zeroIndex < size and nums[zeroIndex] != 0:
#                 zeroIndex += 1
#             numIndex = zeroIndex
#             while numIndex < size and nums[numIndex] == 0 :
#                 numIndex += 1
#             if numIndex < size and zeroIndex < size:
#                 nums[zeroIndex],nums[numIndex] = nums[numIndex],nums[zeroIndex]
                
"""
time Complexity: O(n)
space Complexity: O(1)

"""
            
            
        
            
            
            
            