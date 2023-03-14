class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        left = 0
        right = len(arr)-1

        while left < right:
            middle = left + (right-left)//2

            if arr[middle-1] < arr[middle] < arr[middle+1]:
                left = middle
            elif arr[middle-1] > arr[middle] > arr[middle+1]:
                right = middle
            else:
                return middle