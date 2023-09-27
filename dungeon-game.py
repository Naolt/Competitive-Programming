class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """

        def bp():
            grid = [[float("inf")]*(len(dungeon[0])+1) for i in range(len(dungeon)+1)]
            grid[-1][-1] = 0 if dungeon[-1][-1] > 0 else -1*dungeon[-1][-1]+1 
            for row in range(len(grid)-1,0,-1):
                for col in range(len(grid[0])-1,0,-1): 

                    grid[row-1][col] = max(0,min(grid[row-1][col],max(grid[row][col],1)+dungeon[row-1-1][col-1]*-1))
                    grid[row][col-1] = max(0,min(grid[row][col-1],max(grid[row][col],1)+dungeon[row-1][col-1-1]*-1))

            return grid[1][1] or 1

        return bp()