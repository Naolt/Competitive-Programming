class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        left = 0
        right = len(nums)-1
        count = 0
        nums.sort()
        
        while left < right:
            numSum = nums[left] + nums[right]
            if numSum == k:
                left += 1
                right -= 1
                count += 1
            elif numSum < k:
                left += 1
            else:
                right -= 1
                
        return count