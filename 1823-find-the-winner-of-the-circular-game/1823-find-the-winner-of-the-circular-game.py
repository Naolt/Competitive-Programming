class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        counter = 0
        sit = [x for x in range(1,n+1)]
        removed = 0
        counter = 0
        if n == 1:
            return n
        
        
        while counter < n:
            count = k
            while count > 0:
                if sit[counter] !=  0:
                    count -= 1
                if count == 0:
                    break
                else:
                    if counter == n-1:
                        counter = 0
                    else:
                        counter += 1
                    
            sit[counter] = 0
            removed += 1
            
            if removed == n-1:
                return max(sit)
            
            
            
                
               
            
            
        
        
            