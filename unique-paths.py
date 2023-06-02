class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.getPath2(m,n)

    def getPath(self,r,c,m,n,memo):
        if r == m-1 and c == n-1:
            return 1

        if (r,c) in memo:
            return memo[(r,c)]

        total = 0
        if self.inBound(r,c+1,m,n):
            right = self.getPath(r,c+1,m,n,memo)
            total += right 
        if self.inBound(r+1,c,m,n):
            down = self.getPath(r+1,c,m,n,memo)
            total += down
        
        memo[(r,c)] = total

        return total 
    
    def inBound(self,r,c,m,n):
        return (0 <= r < m) and (0 <= c < n)

    def getPath2(self,m,n):
        grid = [[0 for i in range(n)] for j in range(m)]
        grid[0][0] = 1
        
        for row in range(m):
            for col in range(n):
                val = 0
                if row - 1 >= 0:
                    val += grid[row-1][col]
                if col - 1 >= 0:
                    val += grid[row][col-1]
                grid[row][col] += val

        return grid[m-1][n-1]