class Solution:
    def knightDialer(self, n: int) -> int:
        position={1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2),0:(3,1)}
        directions=[(2,-1),(2,1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
        mod = (10**9) + 7
        def checkInbound(row,col):
            return ((0<=row<3) and (0<=col<3)) or (row==3 and col==1)
        
        @cache
        def getPath(n,i,j):
            
            if n == 0:
                return 1
            
            total = 0
            for x,y in directions:
                r = i + x
                c = j + y
                if checkInbound(r,c):
                    total += getPath(n-1,r,c) % mod
            
            return total
        
        total = 0

        for i in range(10):
            total += getPath(n-1,position[i][0],position[i][1])
        
        return total % mod