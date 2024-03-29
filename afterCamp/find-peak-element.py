class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums)-1

        while left < right:
            mid = left + (right-left)//2

            if mid+1 <= right and nums[mid] < nums[mid+1]:
                left = mid+1
            elif mid-1 >= left and nums[mid] < nums[mid-1]:
                right = mid-1
            else:
                left = mid
                break

        return left