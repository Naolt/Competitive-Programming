class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums)

        while left+1<right:
            middle = math.floor(left + (right-left)/2)

            if nums[middle] < target:
                left =  middle
            else:
                right = middle
        return left+1