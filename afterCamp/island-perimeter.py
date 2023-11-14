class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        def inBound(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        direc = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        def dfs(row,col):
            if not inBound(row,col) or not grid[row][col]:
                return 1
            visited.add((row,col))
            res = 0
            for x,y in direc:
                if (row+x,col+y) not in visited:
                    res += dfs(row+x,col+y)

            return res

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)

        return 0