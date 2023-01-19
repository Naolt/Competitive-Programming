class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        size = len(matrix)
        colSize = len(matrix[0])
        
        for row in range(size):
            if matrix[row][colSize-1] >= target:
                for num in matrix[row]:
                    if num == target:
                        return True
                return False
                