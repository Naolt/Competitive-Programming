class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result= [-1]*2
        # bisect left
        left = -1
        right = len(nums)
        if not nums:
            return result
        
        
        while left+1 < right:
            middle = math.floor(left + (right-left)/2)
            if nums[middle] < target:
                left = middle
            else:
                right = middle
        print(left)
        if left+1 >= len(nums):
            return result
        if nums[left+1] != target:
            return result
        result[0] = left+1
        #bisect right
        left = -1
        right = len(nums)
        while left+1 < right:
            middle = math.floor(left + (right-left)/2)
            if nums[middle] <= target:
                left = middle
            else:
                right = middle
        
        result[1] = left
        
        return result