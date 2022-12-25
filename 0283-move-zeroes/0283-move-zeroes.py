"""
nums = [3,0,12,0,0]
        i
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
        
        zeroFinder = 0
        numFinder = 0
        size = len(nums)
        
        while(numFinder < size and zeroFinder < size):
            
            if(nums[zeroFinder] != 0):
                while True:
                    zeroFinder += 1
                    if zeroFinder >= size or nums[zeroFinder] == 0:
                        break
            if zeroFinder > numFinder:
                numFinder = zeroFinder
            if(numFinder < size and nums[numFinder] == 0):
                while True:
                    
                    numFinder += 1
                    if numFinder >= size or nums[numFinder] != 0:
                        break
            if numFinder > zeroFinder and numFinder < size and zeroFinder < size:
                nums[zeroFinder],nums[numFinder] = nums[numFinder],nums[zeroFinder]
            else:
                break
            
            
            
            