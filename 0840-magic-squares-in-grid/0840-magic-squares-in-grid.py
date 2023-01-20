from collections import defaultdict
class Solution:
    
    def checkGrid(self,grid,i,j)->bool:
        vertical = grid[i][j] + grid[i][j+1] + grid[i][j+2]
        horizontal = grid[i][j] + grid[i+1][j] + grid[i+2][j]
        d1 = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
        d2 = grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2]
        
        return (self.checkEqual(grid,i,j) and (vertical == horizontal == d1 == d2))
    def checkEqual(self,grid,i,j)->bool:
        sameElem = defaultdict(int)
        for row in range(3):
            for col in range(3):
                if 0 < grid[i+row][j+col] < 10:
                    sameElem[grid[i+row][j+col]] += 1
        
        if len(sameElem) == 9:
            print(i,j)
            return True
        return False
    
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        
        
        rowSize = len(grid)
        colSize = len(grid[0])
        
        i = 0
        j = 0
        
        if rowSize < 3 and colSize < 3:
            return 0
        
        while i + 3 <= rowSize:
            while j + 3 <= colSize:
                
            
                if self.checkGrid(grid,i,j):
                    count += 1
                j += 1
            j = 0
            i += 1
            
        return count
        
                    