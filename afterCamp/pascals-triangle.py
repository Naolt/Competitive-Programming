class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        grid = [[1]]

        for row in range(1,numRows):
            newRow = [0]*(row+1)
            for index,val in enumerate(grid[row-1]):
                newRow[index] +=  val
                newRow[index+1] +=  val
            grid.append(newRow[:])

        return grid 

