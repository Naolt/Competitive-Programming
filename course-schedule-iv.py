class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        grid = [[float('inf')]*numCourses for i in range(numCourses)]

        for row,col in prerequisites:
            grid[row][col] = 1

        for i in range(numCourses):
            grid[i][i] = 0
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    grid[i][j] = min(grid[i][j],grid[i][k]+grid[k][j])
                
        answer = []
        
        for row,col in queries:
            if grid[row][col] == float("inf"):
                answer.append(False)
            else:
                answer.append(True)

        return answer