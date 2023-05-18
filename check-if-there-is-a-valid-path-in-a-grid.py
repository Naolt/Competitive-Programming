class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rowSize = len(grid)
        colSize = len(grid[0])
        graph = UnionSet(rowSize,colSize)

        neighbors = {
                  1: [(0, -1, {1, 4, 6}), (0, 1, {1, 3, 5})],
                  2: [(-1, 0, {2, 5, 6}), (1, 0, {2, 3, 4})],
                  3: [(0, -1, {1, 4, 6}), (1, 0, {2, 5, 6})],
                  4: [(1, 0, {2, 5, 6}), (1, 0, {2, 3, 4})],
                  5: [(-1, 0, {2, 3, 4}), (0, -1, {1, 4, 6})],
                  6: [(-1, 0, {2, 3, 4}), (0, 1, {1, 3, 5})]
              }
        

        for row in range(rowSize):
            for col in range(colSize):
                
                for r,c,allowed in neighbors[grid[row][col]]:
                    newRow = row + r
                    newCol = col + c
                    if self.inBound(newRow,newCol,rowSize,colSize) and grid[newRow][newCol] in allowed:
                        graph.union((row,col),(newRow,newCol))
        
        return graph.onSamePath((0,0),((rowSize-1),(colSize-1)))
                

    def inBound(self,row,col,rowSize,colSize):
        return (0 <= row < rowSize) and (0 <= col < colSize)
        

class UnionSet:
    def __init__(self,row,col):
        self.rep = {(r,c):(r,c) for r in range(row) for c in range(col)}
        self.size = {(r,c):1 for r in range(row) for c in range(col)}

    def find(self,num):
        root = num
        while root != self.rep[root]:
            root = self.rep[root]
        
        while num != self.rep[num]:
            parent = self.rep[num]
            self.rep[num] = root
            num = parent
        
        return root

    def union(self,num1,num2):
        rep1 = self.find(num1)
        rep2 = self.find(num2)

        if rep1 == rep2:
            return

        if self.size[rep1] > self.size[rep2]:
            self.size[rep1] += self.size[rep2]
            self.rep[rep2] = rep1
        else:
            self.size[rep2] += self.size[rep1]
            self.rep[rep1] = rep2
    
    def onSamePath(self,num1,num2):
        rep1 = self.find(num1)
        rep2 = self.find(num2)

        return rep1 == rep2