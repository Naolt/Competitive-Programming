class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        size = len(grid)
        
        maxLocal = [[0]*(size-2) for _ in range(size-2)]
        
        for row in range(size-2):
            
            for col in range(size-2):
                currentMax = 0
                for i in range(3):
                    for j in range(3):
                        if 0 <= row+i < size and 0 <= col + j < size:
                            currentMax=max(currentMax,grid[row+i][col+j])
                maxLocal[row][col] = currentMax
                
        return maxLocal