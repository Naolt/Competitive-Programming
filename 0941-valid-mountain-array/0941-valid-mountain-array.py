class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak = -1
        peakFound = False
        
        if len(arr) <= 2:
            return False
            
        
        for num in arr:
            if num > peak:
                if peakFound:
                    return False
                peak = num
            elif num < peak:
                if not peakFound:
                    peakFound = True
                peak = num
            else:
                return False
        if peakFound == False or arr[0] > arr[1]:
            return False
        return True