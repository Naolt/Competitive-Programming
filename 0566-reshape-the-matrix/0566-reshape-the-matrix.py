class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        reshaped = [[]*c for x in range(r)]
        rowSize = len(mat)
        colSize = len(mat[0])
        rowCounter = 0
        colCounter = 0
        
        if rowSize * colSize != r*c:
            return mat
        
        for row in range(rowSize):
            for col in range(colSize):
                reshaped[rowCounter].append(mat[row][col])
                colCounter += 1
                print(rowCounter,colCounter,r,c)
                if colCounter == c:
                    colCounter =  0
                    rowCounter += 1
                    
        return(reshaped)
                