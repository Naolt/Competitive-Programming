class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:

        row_size = len(grid)
        col_size = len(grid[0])
        answer = 0

        prefix = self.calcPrefix(grid)

        for i in range(row_size-2):
            for j in range(col_size-2):
                bottom_right = prefix[i+3][j+3]
                bottom_left_prev = prefix[i+3][j]
                top_right_prev = prefix[i][j+3]
                top_left_prev = prefix[i][j]

                total = bottom_right - bottom_left_prev - top_right_prev + top_left_prev
                total -= grid[i+1][j]
                total -= grid[i+1][j+2]

                answer = max(answer,total)
                
        return answer

        

    def calcPrefix(self,grid):
        
        row_size = len(grid)
        col_size = len(grid[0])

        prefix = [[0]*(col_size+1)]

        for row in grid:
            acc = [0]+list(accumulate(row))
            prefix.append(acc)

        for col in range(len(prefix[0])):
            for row in range(1,row_size):
                prefix[row+1][col] += prefix[row][col]

        return prefix
