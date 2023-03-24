class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [-1]*(len(nums)+1)
        for num in nums:
            arr[num] = 1
        for index,num in enumerate(arr):
            if num == -1:
                return index