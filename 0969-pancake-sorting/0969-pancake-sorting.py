class Solution:
    def flip(self,arr,start,end):
        while start < end:
            arr[start],arr[end] =  arr[end],arr[start]
            start += 1
            end -= 1
            
    def findMax(self,arr,n):
        maxIndex = 0
        for i in range(n):
            if arr[i] > arr[maxIndex]:
                maxIndex = i
        return maxIndex
        
    def pancakeSort(self, arr: List[int]) -> List[int]:
        answer = []
        size = len(arr)
        pos = size-1
        
        for i,value in enumerate(arr):
            maxIndex = self.findMax(arr,pos+1)
            
            self.flip(arr,0,maxIndex)
            self.flip(arr,0,pos)
            answer.append(maxIndex+1)
            answer.append(pos+1)
            pos -= 1
                
        return answer
        
            
            
                
            
            