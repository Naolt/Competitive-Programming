class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = max(self.dfs(grid,i,j,0),area)                
        return area


    def dfs(self,grid,row,col,count):
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        if not self.isInBound(row,col,grid) or grid[row][col] == 0:
            return 0
        grid[row][col] = 0
        # visited.add((row,col))
        total = 0
        for direction in directions:
            newRow = row + direction[0]
            newCol = col + direction[1]
            total += self.dfs(grid,newRow,newCol,count+1)
        return total + 1

    def isInBound(self,row,col,grid):
        return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))