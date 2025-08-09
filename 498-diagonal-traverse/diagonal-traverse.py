class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        
        res = []

        i,j,up = 0,0,True

        def inbound(i,j):
            return 0 <= i < len(mat) and 0 <= j < len(mat[0])

        def getNext(i,j,up):
            if up:
                i += 1
                if not inbound(0,j):
                    i += 1
                    j -= 1
            else:
                j += 1 
                if not inbound(i,0):
                    i -= 1
                    j += 1
                
            return i,j, not up

        while True:
            res.append(mat[i][j])
            direc = [-1,1] if up else [1,-1]
            i += direc[0]
            j += direc[1]
            
            if not inbound(i,j):
                i,j,up = getNext(i,j,up)
                if not inbound(i,j):
                    return res
