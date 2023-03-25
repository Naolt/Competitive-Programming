class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        left = 1
        right = size

        while left < right:
            middle = left + (right - left)//2
            smallCount = 0

            for i in range(size):
                if nums[i] <= middle:
                    smallCount += 1
            
            if smallCount > middle:
                right = middle
            else:
                left = middle+1
            print(left,right,middle)

        return left