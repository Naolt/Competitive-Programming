class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        size = len(arr)        
        if size == 1:
            return 1
        result = 1
        left = 0
        flag = True
        if arr[0] < arr[1]:
            flag = False
        
        for right in range(size-1):
            if flag:
                if right % 2 == 0:
                    if arr[right] < arr[right+1]:
                        result = max(result,right-left+1)
                        left = right
                        flag = False
                else:
                    if arr[right] > arr[right+1]:
                        result = max(result,right-left+1)
                        left = right
                        flag = False
                    
            else:
                if right % 2 == 0:
                    if arr[right] > arr[right+1]:
                        result = max(result,right-left+1)
                        left = right
                        flag = True      
                else:   
                    if arr[right] < arr[right+1]:
                        result = max(result,right-left+1)
                        left = right
                        flag = True
            if arr[right] == arr[right+1]:
                result = max(result,right-left+1)
                left = right + 1
                if left < size-1:
                    if arr[left] > arr[left+1]:
                        flag = True
                    else:
                        flag = False 
                result = max(result,right-left+1)
        if left < size-1:
            result = max(result,size-left)
                
        return result
                    
                        
                        