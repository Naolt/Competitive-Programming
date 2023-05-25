class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        arr.sort()
        size = len(arr)
        if arr[0] != 1:
            arr[0] = 1
            
        for i in range(size-1):
            if abs(arr[i]-arr[i+1]) > 1:
                arr[i+1] = arr[i] + 1
        
        return arr[-1]