class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        total = 0
        total2 = 0
        
        for i in range(size):
            total +=i
            total2+=nums[i]
            
        return total+size-total2