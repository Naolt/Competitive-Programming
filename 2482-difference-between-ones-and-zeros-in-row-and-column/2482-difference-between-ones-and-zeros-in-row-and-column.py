from collections import defaultdict
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        colCount = defaultdict(int)
        colSize = len(grid[0])
        rowSize = len(grid)
        
        newGrid = []
      
        for row in range(rowSize):
            rowCount = 0
            for col in range(colSize):
               
                rowCount += grid[row][col]
                colCount[col] += grid[row][col]
            newList = []
            for col in range(colSize):
                newList.append((rowCount - (rowSize-rowCount)))
               
            newGrid.append(newList)
            
        for row in range(rowSize):
            for col in range(colSize):
                newGrid[row][col] += (colCount[col]-(colSize- colCount[col] ))
                
        return newGrid
        