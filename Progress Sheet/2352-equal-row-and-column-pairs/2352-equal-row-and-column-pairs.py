class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        size = len(grid)
        count = 0
        inversed = list(zip(*grid))
        
        for row in range (size):
            for col in range(size):
                if( list(grid[row]) == list(inversed[col])):
                    count += 1
                
        return count
                
        
        
                
            
           
                