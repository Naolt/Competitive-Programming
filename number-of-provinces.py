class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        mySet = set()
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]:
                    count += 1
                    self.checkConnected(isConnected,j,mySet)
        return count

    def checkConnected(self,grid,col,visited):
        if col in visited:
            return
        visited.add(col)
        for i in range(len(grid[0])):
            if grid[col][i] == 1:
                grid[col][i] = 0
                grid[i][col] = 0
                self.checkConnected(grid,i,visited)    
        return

    def inBound(self,row,col,grid):
        return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))