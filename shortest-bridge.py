class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        rowSize,colSize = len(grid),len(grid[0])
        island = set()
        found = False
        for row in range(rowSize):
            for col in range(colSize):
                if grid[row][col] == 1:
                    island.add((row,col))
                    self.getIsland(grid,(row,col),island,directions)
                    found = True
                    if found: break
            if found: break

        queue = deque(list(island))
        count = 0

        while queue:
            size = len(queue)
            for i in range(size):
                row,col = queue.popleft()

                for r,c in directions:
                    newRow = row + r
                    newCol = col + c

                    if self.inBound(grid,newRow,newCol) and ((newRow,newCol) not in island):
                        if grid[newRow][newCol] == 1:
                            return count
                        queue.append((newRow,newCol))
                        island.add((newRow,newCol))
                    
            count += 1
        return 0

    def getIsland(self,grid,start,island,directions):
        row,col = start
        for r,c in directions:
            newRow = row + r
            newCol = col + c
            if self.inBound(grid,newRow,newCol) and ((newRow,newCol) not in island) and grid[newRow][newCol] == 1:
                island.add((newRow,newCol))
                self.getIsland(grid,(newRow,newCol),island,directions)

    def inBound(self,grid,row,col):
        return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))