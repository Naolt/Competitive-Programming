class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        
        res = []

        i,j,up = 0,0,True

        def inbound(i,j):
            return 0 <= i < len(mat) and 0 <= j < len(mat[0])

        def getNext(i,j,up):
            
            # if I is out of bound
            if up:
                if not inbound(0,j):
                    i += 2
                    j -= 1
                else:
                    i += 1
                
                return i,j,False
            else:
                if not inbound(i,0):
                    i -= 1
                    j += 2
                else:
                    j += 1
                
                return i,j,True

                    

        while True:
            res.append(mat[i][j])
            if up:
                i -= 1
                j += 1
            else:
                i += 1
                j -= 1
            
            if not inbound(i,j):
                i,j,up = getNext(i,j,up)
                # print("new start",i,j,up)
                if not inbound(i,j):
                    return res
            # else:
                # res.append(mat[i][j])
