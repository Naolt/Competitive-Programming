"""
 0 1 2 3 4 5
[2,3,1,2,4,3]
           l
             r 

current = 3
length = 4
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,right= 0, 0
        result = float('inf')
        size = len(nums)
        current = 0
        
        while right <= size and left < size:
            
            if current < target:
                if right >= size:
                    break
                current += nums[right]
                right += 1
            else:
                result = min(result,right-left)
                current -= nums[left]
                left += 1
            
        if result > 100000:
            return 0
        return result