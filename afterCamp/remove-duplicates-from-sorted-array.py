class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        for i in range(1,len(nums)):
            right = i
            while right < len(nums) and nums[right] <= nums[i-1]:
                right += 1
            if right == len(nums):
                return i
            
            nums[i] = nums[right]
        
        return len(nums)