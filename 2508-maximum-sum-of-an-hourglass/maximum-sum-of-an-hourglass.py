class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:

        row_size = len(grid)
        col_size = len(grid[0])
        answer = 0

        for i in range(row_size-2):
            for j in range(col_size-2):
                total = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                answer = max(answer,total)

        return answer

        

    # def calcHourTime(self,grid,row,col):
        
    #     # print("Start",row,col,grid[row][col])
        

    #     return total

        