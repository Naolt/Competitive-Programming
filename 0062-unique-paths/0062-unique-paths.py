class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #bottom up
        
        grid = [[0]*(n+1) for i in range(m+1)]
        
        grid[1][1] = 1
        
        for row in range(1,m+1):
            for col in range(1,n+1):
                if row == 1 and col == 1:
                    continue
                grid[row][col] = grid[row-1][col] + grid[row][col-1]
        
        return grid[-1][-1]