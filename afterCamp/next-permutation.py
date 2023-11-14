class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) == 1:
            return 
        swapped = False
        
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                swapped = True
                minIndex = i+1
                for j in range(i+1,len(nums)):
                    if nums[j] > nums[i] and nums[minIndex] > nums[j]:
                        minIndex = j
                
                nums[i],nums[minIndex] = nums[minIndex],nums[i]
                
                for j in range(i+1,len(nums)):
                    for k in range(i+1,len(nums)-1):
                        if nums[k] > nums[k+1]:
                            nums[k],nums[k+1] = nums[k+1],nums[k]
                break
                   
        
        if not swapped:
           nums.sort()
        


