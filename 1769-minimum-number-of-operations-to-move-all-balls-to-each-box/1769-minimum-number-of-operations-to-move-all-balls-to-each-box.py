class Solution:
    def setOperation(self,boxes,answer,start,end,index):
        for i in range(start,end):
           
            if boxes[i] == "1":
             
                answer[index] += abs(i-index)
                
            
        
    def minOperations(self, boxes: str) -> List[int]:
        
        size = len(boxes)
        answer = [0]*size
        
        for i in range(size):

            self.setOperation(boxes,answer,0,i,i)
          
            self.setOperation(boxes,answer,i+1,size,i)
        return answer