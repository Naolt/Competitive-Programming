class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        size = len(grid[0])
        first= list(accumulate(grid[0]))
        second= list(accumulate((grid[1][::-1])))[::-1]
        minValue = float('inf')
                
        for i in range(size):
            minValue = min(minValue,max((first[-1]-first[i]) , (second[0]-second[i])))

        return minValue