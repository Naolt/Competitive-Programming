class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        rowSize = len(mat)
        colSize = len(mat[0])
        queue = deque()
        result = [[0]*colSize for i in range(rowSize)]
        for row in range(rowSize):
            for col in range(colSize):
                if mat[row][col] == 0:
                    queue.append((row,col))

        while queue:
            size = len(queue)
            for i in range(size):
                row,col = queue.popleft()

                for r,c in directions:
                    newRow = row + r
                    newCol = col + c
                    if self.inBound(newRow,newCol,mat) and mat[newRow][newCol] == 1:
                        queue.append((newRow,newCol)) 
                        mat[newRow][newCol] = 0
                        result[newRow][newCol] = result[row][col] + 1

        return result



    def inBound(self,row,col,grid):
        return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))