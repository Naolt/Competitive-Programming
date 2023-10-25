class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        rep = [[(i,j) for j in range(len(grid))] for i in range(len(grid[0]))]
        size = [[0]*len(grid) for j in range(len(grid))]

        def find(row,col):
            member = (row,col)
            while rep[row][col] != (row,col):
                row,col = rep[row][col]
            
            startr,startc = member
            while rep[startr][startc] != (row,col):
                parent = rep[row][col]
                rep[row][col] = (row,col)
                startr,startc = parent
            
            return (row,col)

        def union(member1,member2):
            r1,c1 = member1
            r2,c2 = member2
            p1,p2 = find(r1,c1),find(r2,c2)
            
            if p1 == p2:
                return
            
            if size[p1[0]][p1[1]] > size[p2[0]][p2[1]]:
                rep[p2[0]][p2[1]] = p1
                size[p1[0]][p1[1]] += size[p2[0]][p2[1]]
            else:
                rep[p1[0]][p1[1]] = p2
                size[p2[0]][p2[1]] += size[p1[0]][p1[1]]


        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        zeros = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 0:
                    zeros.append((i,j))
                else:
                    size[i][j] = 1

        def isInBound(row,col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0])) 
        
        def findIsland(row,col,visited):

            visited.add((row,col))
            for r,c in directions:
                if isInBound(row+r,col+c) and grid[row+r][col+c] and (row+r,col+c) not in visited:
                    # parent = find(row+r,col+c)
                    # if parent == (row+r,col+c):
                    union((row,col),(row+r,col+c))
                    findIsland(row+r,col+c,visited)
        
        if not zeros:
            return len(grid)*len(grid)

        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j]:
                    findIsland(i,j,visited)
        
        val = defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j]:
                    parent = find(i,j)
                    val[parent] += 1

        maxArea = 0
        for row,col in zeros:
            parents = set()
            total = 1
            for r,c in directions:
                newR = row+r
                newC = col+c
                if not isInBound(newR,newC):
                    continue
                parent = find(newR,newC)
                if parent not in parents:
                    total += val[parent]
                    parents.add(parent)
            maxArea = max(maxArea,total)

        
        return maxArea