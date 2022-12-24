"""
arr = [0,0,0,0]
           i
             j
holder1 = 0
 holder2 = 0


approach:

- iterate through the array when a zero is found put the next element on holder1 and next+1 on holder2
  then make the next element 0 and 


"""
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        i = 0 
        j = 0
        size = len(arr)
        while i < size:
            holder1 = None
            holder2 = None
            if arr[i] == 0:
                j = i+1
                if(j >= size - 1):
                    if j == size -1:
                        arr[j] = 0
                    break
                holder1 = arr[j]
                holder2 = arr[j+1]
                arr[j] = 0
                
                while j < size-1:
                    arr[j+1] = holder1
                    j += 1
                    holder1 = holder2
                    if(j+1 != size):
                        holder2 = arr[j+1]
                
                i+=2
            else:
                i+=1
        
                
                
                
                