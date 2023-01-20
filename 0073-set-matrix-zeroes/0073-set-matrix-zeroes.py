class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        vertical = {}
        horizontal=  {}
        
        rowSize = len(matrix)
        colSize = len(matrix[0])
        for row in range(rowSize):
            for col in range(colSize):
                if matrix[row][col] == 0:
                    vertical[col] = 1
                    horizontal[row] = 1
        for row in range(rowSize):
            for col in range(colSize):
                if row in horizontal:
                    matrix[row][col] = 0
                if col in vertical:
                    matrix[row][col] = 0
                    
        