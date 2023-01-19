class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        diag = {}
        
        rowSize = len(matrix)
        colSize = len(matrix[0])
        
        for row in range(rowSize):
            for col in range(colSize):
                if (row - col) not in diag:
                    diag[row-col] = [matrix[row][col]]
                else:
                    if diag[row-col][0] != matrix[row][col]:
                        return False
                    
                    
        return True
                    