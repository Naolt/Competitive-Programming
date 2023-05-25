class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        arr.sort()
        
        size = len(arr)
        if arr[0] != 1:
            arr[0] = 1
        j = 0
        
        while j < size-1:
            i = j
            while i < size-1 and abs(arr[i+1] - arr[i]) > 1:
                arr[i+1] = arr[i]+1
                i += 1
            j = i
            j += 1
        
        return arr[-1]