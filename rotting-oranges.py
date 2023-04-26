class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        return self.bfs(grid)
    
    def bfs(self,grid):
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        rotten = []
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1

        queue = deque(rotten)
        visited = set(rotten)
        count = -1
        while queue:
            count += 1
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                for row,col in directions:
                    newRow = node[0] + row
                    newCol = node[1] + col
                    if self.inBound(newRow,newCol,grid) and ((newRow,newCol) not in visited) and (grid[newRow][newCol] == 1):
                        queue.append((newRow,newCol))
                        visited.add((newRow,newCol))
                        fresh -= 1
                    
        print(fresh)
        if fresh > 0:
            return -1
        return count if count != -1 else 0

    def inBound(self,row,col,grid):
        return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))