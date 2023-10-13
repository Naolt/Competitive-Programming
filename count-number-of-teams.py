class Solution:
    def numTeams(self, rating: List[int]) -> int:
        size = len(rating)
        @cache
        def dp(index,last,count,inc):
                
            if count == 3:
                return 1
            if index >= size:
                return 0
            add,noAdd = 0,0
            
            for i in range(index,size):
                if not count:
                        myNum = rating[i]
                        add += dp(i+1,myNum,count+1,inc)
                      
                else:
                    
                    if (inc and last < rating[i]) or (not inc and last > rating[i] ):
                        myNum = rating[i]
                        add += dp(i+1,myNum,count+1,inc)

            return add + noAdd
        
        return dp(0,-inf,0,True) + dp(0,inf,0,False)