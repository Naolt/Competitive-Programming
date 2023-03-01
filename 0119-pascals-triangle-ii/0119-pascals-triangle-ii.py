class Solution:
    
    def __init__(self):
        self.memo = {} 
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        arr = [1]*(rowIndex+1)
        newArr = self.getRow(rowIndex-1)
        
        for i in range(1,math.ceil((rowIndex+1)/2)):
            numSum = sum(newArr[i-1:i+1])
            arr[i] = numSum
            arr[rowIndex-i] = numSum 
            
        return arr