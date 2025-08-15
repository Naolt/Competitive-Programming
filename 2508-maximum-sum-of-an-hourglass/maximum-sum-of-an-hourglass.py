class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:

        row_size = len(grid)
        col_size = len(grid[0])
        answer = 0

        for i in range(row_size-2):
            for j in range(col_size-2):
                result = self.calcHourTime(grid,i,j)
                print((i,j),result)
                answer = max(answer,result)

        return answer

        

    def calcHourTime(self,grid,row,col):
        
        total = 0
        for i in range(row,row+3):
            for j in range(col,col+3):
                total += grid[i][j]

        total -= grid[row+1][col]
        total -= grid[row+1][col+2]

        return total

        
