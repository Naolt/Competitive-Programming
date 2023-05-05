class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set([tuple(entrance)])
        queue = deque([tuple(entrance)])
        def inBound(row,col):
            return (0 <= row < len(maze)) and (0 <= col < len(maze[0]))
        def isExit(row,col):
            return row == 0 or row == len(maze)-1 or col == 0 or col == len(maze[0])-1
        count = 0
        while queue:
            size = len(queue)
            for i in range(size):
                # print(queue)
                row,col = queue.popleft()

                for r,c in directions:
                    newRow = row + r 
                    newCol = col + c
                    
                    if inBound(newRow,newCol) and maze[newRow][newCol] == '.' and isExit(newRow,newCol) and (newRow,newCol) not in visited:
                        # print("found",(row,col),(r,c),(newRow,newCol),visited)
                        return count + 1

                    if inBound(newRow,newCol) and maze[newRow][newCol] == '.' and (newRow,newCol) not in visited:
                        queue.append((newRow,newCol))
                        visited.add((newRow,newCol))
            count += 1
        return -1