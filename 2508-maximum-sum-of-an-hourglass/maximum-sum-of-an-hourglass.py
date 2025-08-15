class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:

        row_size = len(grid)
        col_size = len(grid[0])
        answer = 0

        for i in range(row_size-2):
            for j in range(col_size-2):
                total = 0
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        # print(f"Element {(i,j)}",grid[i][j])
                        total += grid[r][c]

                # print(f"removing {(row+1,0)} and {(row+1,col+2)}")
                total -= grid[i+1][j]
                total -= grid[i+1][j+2]
                answer = max(answer,total)

        return answer

        

    # def calcHourTime(self,grid,row,col):
        
    #     # print("Start",row,col,grid[row][col])
        

    #     return total

        