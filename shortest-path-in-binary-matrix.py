class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rowSize = len(grid)
        colSize = len(grid[0])
        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        queue = deque([(0,0)])
        count = 0
        while queue:
            size = len(queue)
            count += 1
            for i in range(size):
                cellRow,cellCol = queue.popleft()
                if grid[cellRow][cellCol] == 1:
                    return -1
                
                for row,col in directions:
                    newRow = cellRow + row 
                    newCol = cellCol + col
                    if newRow == rowSize-1 and newCol == colSize-1 and grid[newRow][newCol] == 0:
                        return count+1
                    if self.inBound(rowSize,colSize,newRow,newCol) and grid[newRow][newCol] == 0 and  (newRow,newCol) not in visited:
                        queue.append((newRow,newCol))
                        visited.add((newRow,newCol))
            if cellRow == rowSize-1 and cellCol == colSize-1 and grid[cellRow][cellCol] == 0:
                return count
        return -1

    def inBound(self,rowSize,colSize,row,col):
        return (0 <= row < rowSize) and (0 <= col < colSize)