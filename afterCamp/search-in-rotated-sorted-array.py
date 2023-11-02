class Solution:
    def search(self, nums, target) -> int:
        low,high = 0, len(nums)-1
        
        while low < high:
            middle = low + (high - low)//2
            
            if nums[middle] > nums[high]:
                low = middle+1
            else:
                high = middle
    
        low = low%len(nums)
        high = len(nums)+low
        
        while low <= high:
            middle = low + (high - low)//2
            midIndex = middle%len(nums)
            if nums[midIndex] > target:
                high = middle-1
            else:
                if nums[midIndex] == target:
                    return midIndex
                low = middle+1   
        if nums[low % len(nums)] == target:
            return low % len(nums)
        return -1