class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        size = len(arr)
        
        if len(arr) < 2:
            arr[-1] = -1
            return arr
        
        currentMax = max(arr[1::])
        arr[0] = currentMax
        
        for i in range(2,size):
            if arr[i-1] == currentMax:
                currentMax = max(arr[i::])
                arr[i-1] = currentMax
            else:
                arr[i-1] = currentMax
            
            
        arr[-1] = -1
        return arr
                
            